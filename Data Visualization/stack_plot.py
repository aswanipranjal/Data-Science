import matplotlib.pyplot as plt

days = 		[1, 2, 3, 4, 5]

sleeping = 	[7, 8, 6, 1, 7]
eating = 	[2, 3, 2, 1, 2]
working = 	[7, 8, 4, 1, 5]
playing = 	[3, 5, 7, 1, 8]
programming = [5, 0, 5, 20, 2]

plt.stackplot(days, 
	sleeping, eating, working, playing, programming, 
	colors=['m', 'c', 'r', 'k', 'b'], 
	labels=['Sleeping', 'Eating', 'Working', 'Playing', 'Programming'])

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Interesting graph')
plt.show()