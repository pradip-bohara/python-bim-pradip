
# Matplotlib Labels and Title
'''With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis.'''
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()

# Set Font Properties for Title and Labels
"""You can use the fontdict parameter in xlabel(), ylabel(), and title() to set font properties for the title and labels."""


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1)
plt.xlabel("Average Pulse", fontdict = font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.plot(x, y)
plt.grid()
plt.show()

# Add Grid Lines to a Plot
# With Pyplot, you can use the grid() function to add grid lines to the plot
# plt.grid(axis = 'x')
# plt.grid(axis = 'y')