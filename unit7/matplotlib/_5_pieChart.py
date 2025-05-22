# Matplotlib Pie Charts
''''Creating Pie Charts
With Pyplot, you can use the pie() function to draw pie charts:'''

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 

'''Labels
Add labels to the pie chart with the labels parameter.
The labels parameter must be an array with one label for each wedge:'''

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 

'''Legend
To add a list of explanation for each wedge, use the legend() function:'''
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

'''Box Plot
A box plot shows data distribution and outliers.'''

data = [7, 8, 9, 5, 6, 4, 10, 15, 14, 12, 13]

plt.boxplot(data)
plt.title("Box Plot Example")
plt.show()