import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

# we use labels with the plot function so that the lengend function knows what to put in there
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second line')
# we define axes, titles, legends and labels before we call the show() function
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.legend()
plt.title('Interesting graph\nCheck it out')
plt.show()