import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1) # similar to octave's subplotting system
ax2 = fig.add_subplot(1, 2, 2)

# An animation function is like a draw loop. It'll keep running and animating the plot
def animate_track_record_data(i):
	graph_data = open('C:\\Users\\Aman Deep Singh\\Documents\\Unity-2\\Car AI GA\\Assets\\Data\\fitness.txt', 'r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []
	for line in lines:
		if len(line) > 1:
			x, y = line.split(',')
			xs.append(x)
			ys.append(y)

	# clearing doesn't cost much but is better
	ax1.clear()
	ax1.plot(xs, ys)

def animate_genetic_data(i):
	graph_data = open('C:\\Users\\Aman Deep Singh\\Documents\\Unity-2\\Car AI GA\\Assets\\Data\\data.txt', 'r').read()
	lines = graph_data.split('\n')
	xs = []
	msas = []
	tss = []
	for line in lines:
		if len(line) > 1:
			x, msa, ts, mmt, mbt, com, m, sl, ssa, wd4, wb4, wt4, s2nwd, s, bc1, bc2, am, l2sa, tspd, e = line.split(',')
			xs.append(x)
			msas.append(msa)
			tss.append(ts)
	
	ax2.clear()
	ax2.plot(xs, msas, '--', label='Max Steer Angle')
	ax2.plot(xs, tss, 'b-', label='Top Speed')
	ax2.legend()
# ani stores the reference to the FuncAnimation method instance of the animation class of matplotlib.
# Arguments(where?, function_to_animate, interval_to_animate)
ani1 = animation.FuncAnimation(fig, animate_track_record_data, interval=1000)
ani2 = animation.FuncAnimation(fig, animate_genetic_data, interval=1000)
plt.show();