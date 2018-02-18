import matplotlib.pyplot as plt

days = 		[1, 2, 3, 4, 5]

sleeping = 	[7, 8, 6, 1, 7]
eating = 	[2, 3, 2, 1, 2]
working = 	[7, 8, 4, 1, 5]
playing = 	[3, 5, 7, 1, 8]
programming = [5, 0, 5, 20, 2]

slices = [7, 2, 5, 8, 2];
activities = ['sleeping', 'eating', 'working', 'playing', 'programming'];
colors = ['c', 'm', 'r', 'b', 'k'];
# startangle, shadow are pretty obvious
# explodes accepts a list of arguments whose length is equal to the length of the activities list, 
# and 'brings out' a particular piece of it
# the autopct calculates the percentage each slice occupies
plt.pie(slices, labels=activities, colors=colors, startangle=90, shadow=True, explode=(0, 0.1, 0, 0, 0), autopct='%1.1f%%');

# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
plt.title('Interesting graph')
plt.show()