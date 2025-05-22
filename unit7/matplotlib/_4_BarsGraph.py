# Matplotlib Bars

# Creating Bars
# With Pyplot, you can use the bar()
# function to draw bar graphs:

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink")
plt.show()

'''Bar Color
The bar() and barh() take the keyword 
argument color to set the color of the bars:'''

#================ Histogram ==========
import numpy as np

data = np.random.randn(1000)  # Generate random data
plt.hist(data, bins=30, color='green', alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram Example")
plt.show()