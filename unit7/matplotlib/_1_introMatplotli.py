# Matplotlib 
""" Matplotlib is a comprehensive library for creating static. animated. and interactive
    Visualization in Python. It is particularly useful for data Visualization and graphical ploting
    Matplotlib is open source and we can use it freely.
    Matplotlib is mostly written in python a few segments are written in c, and JS """


# import matplotlib 
# # print(matplotlib.__version__)
import matplotlib.pyplot as plt
""" The plot() Function is used to draw pints (markers) in a diagram.
    By default, the plot() function draws a line form point to pint.
    it takes parameters for specifying points in the diagram.
    Parameter 1 is an array containing the pints on the x-axis.
    Parameter 2 is an array containing the pints on the y-axis.
    """
x =[1,2,3,4,5]  # x-axis
y =[10,20,25,30,40] # y-axis.
# Marker  
"""Markers are used to highlight the data points in a plot. They can be customized in terms of shape size and clor."""
# plt.plot(x, y, marker='o')  # 'o' is the marker style
# plt.title('Plot with Markers')
# plt.show()

plt.plot(x, y, marker='o', linestyle='--', color='red')  # 'o' adds circle markers
plt.show()

"""Common markers:
    'o' Circle
    's' Square
    '^' Triangle 
"""
#Line Styles in Matplotlib
# We can chage line style suing linestyle (ls)
"""Common line styles:

'-' - Solid line
'--' - Dashed line
':' - Dotted line
'-.' - Dash-dot line
"""

# Colors in Matplotlib 
""" Matplotlib allows customizing clors uing clor name or hex codes.
Common color codes:

'r' - Red
'g' - Green
'#ff5733' - Hex code"""

# Format String fmt 
""" You can also use the shortcut string notation parameter to specify the marker.
This parameter is also called fmt, and is written with this syntax:
marker | Line | color """
import numpy as np
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# Marker Size
'''You can use the keyword argument markersize or the shorter version, ms to set the siz of the markers:'''
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# Marker color  keyword argument markeredgecolor or hte shorter mec to set the color of the edge of the markers:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')
plt.show()

plt.plot(ypoints, color = 'r')
plt.show()
"""Line Width
You can use the keyword argument linewidth or the shorter lw to change the width of the line."""
plt.plot(ypoints, linewidth = '20.5')
plt.show()

"""Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:
"""
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()