from __future__ import print_function
import sys

from music21 import *
import numpy as np

from grammar import *
from preprocess import *
from qa import *
import lstm

def __sample(a, temperature=1.0):
	a = np.log(a) / temperature
	a = np.exp(a) / np.sum(np.exp(a))
	return np.argmax(np.random.multinomial(1, a, 1))

def __predict(model, x, indices_val, diversity):
	preds = model.predict(x, verbose=0)[0]
	next_index = __sample(preds, diversity)
	next_val = indices_val[next_index]

	return next_val

def __generate_grammar(model, corpus, abstract_grammars, values, val_indices,
                       indices_val, max_len, max_tries, diversity):
    curr_grammar = ''
    # np.random.randint is exclusive to high
    start_index = np.random.randint(0, len(corpus) - max_len)
    sentence = corpus[start_index: start_index + max_len]    # seed
    running_length = 0.0
    while running_length <= 4.1:    # arbitrary, from avg in input file
        # transform sentence (previous sequence) to matrix
        x = np.zeros((1, max_len, len(values)))
        for t, val in enumerate(sentence):
            if (not val in val_indices): print(val)
            x[0, t, val_indices[val]] = 1.

        next_val = __predict(model, x, indices_val, diversity)

        # fix first note: must not have < > and not be a rest
        if (running_length < 0.00001):
            tries = 0
            while (next_val.split(',')[0] == 'R' or 
                len(next_val.split(',')) != 2):
                # give up after 1000 tries; random from input's first notes
                if tries >= max_tries:
                    print('Gave up on first note generation after', max_tries, 
                        'tries')
                    # np.random is exclusive to high
                    rand = np.random.randint(0, len(abstract_grammars))
                    next_val = abstract_grammars[rand].split(' ')[0]
                else:
                    next_val = __predict(model, x, indices_val, diversity)

                tries += 1

        # shift sentence over with new value
        sentence = sentence[1:] 
        sentence.append(next_val)

        # except for first case, add a ' ' separator
        if (running_length > 0.00001): curr_grammar += ' '
        curr_grammar += next_val

        length = float(next_val.split(',')[1])
        running_length += length

    return curr_grammar

def generate(data_fn, out_fn, N_epochs):
	max_len = 20
	max_tries = 1000
	diversity = 0.5

	bpm = 130

	chords, abstract_grammars = get_musical_data(data_fn)
	corpus, values, val_indices, indices_val = get_corpus_data(abstract_grammars)
	print('Corpus length: ', len(corpus))
	print('Total number of values: ', len(values))

	model = lstm.build_model(corpus=corpus, val_indices=val_indices, max_len=max_len, N_epochs=N_epochs)
	out_stream = stream.Stream()

	curr_offset = 0.0
	loop_end = len(chords)
	for loop_index in range(1, loop_end):
		curr_chords = stream.Voice()
		for j in chords[loop_index]:
			curr_chords.insert((j.offset % 4), j)

		curr_grammar = __generate_grammar(model=model, corpus=corpus,
										  abstract_grammars=abstract_grammars,
										  values=values, val_indices=val_indices,
										  indices_val=indices_val, max_len=max_len,
										  max_tries=max_tries, diversity=diversity)
		curr_grammar = curr_grammar.replace(' A', ' C').replace(' X', ' C')
		curr_grammar = prune_grammar(curr_grammar)
		curr_notes = unparse_grammar(curr_grammar, curr_chords)
		curr_notes = prune_notes(curr_notes)
		curr_notes = clean_up_notes(curr_notes)
		print('After pruning: %s notes' % (len([i for i in curr_notes  if isinstance(i, note.Note)])))
		for m in curr_notes:
			out_stream.insert(curr_offset + m.offset, m)
		for mc in curr_chords:
			out_stream.insert(curr_offset + mc.offset, mc)

		curr_offset += 4.0

	out_stream.insert(0.0, tempo.MetronomeMark(number=bpm))

	play = lambda x: midi.realtime.StreamPlayer(x).play()
	play(out_stream)

	mf = midi.translate.streamToMidiFile(out_stream)
	mf.open(out_fn, 'wb')
	mf.write()
	mf.close()

def main(args):
	try:
		N_epochs = int(args[1])
	except:
		N_epochs = 128

	data_fn = 'data/' + 'original_metheny.mid'
	out_fn = 'data/' + 'deepjaszx_on_metheny...' + str(N_epochs)
	if (N_epochs == 1): out_fn += '_epoch.midi'
	else:				out_fn += '_epochs.midi'
	generate(data_fn, out_fn, N_epochs)

if __name__ == '__main__':
	import sys
	main(sys.argv)