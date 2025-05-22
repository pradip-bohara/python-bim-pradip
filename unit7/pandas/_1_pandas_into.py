#Pandas is powerful Python library used for data manipulation and analysis. 
# it provide two primary data structures 
#       Series - A one dimensional labeled array.
#       DataFrame - A tow dimensional table-like structure.

""" It has functions for analyzing cleaning, exploring and manipulating data.
    The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" 
    and was created by Wes Mckinney in 2008"""

import pandas as pd
print(pd.__version__)

#=============== Series and DataFrames ========= 
# A Series in Pandas is a one-dimensional array with labels (index).
#it is similar ot a column in an Excel sheet.

#Create series
data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
series = pd.Series(data)
print(series)

#Create your own labels:
a = [1,5,7]
tuplast = pd.Series(a, index=["A", "B", "C" ])
print(tuplast)
print(tuplast["C"])

# ou can also use a key/value object, like a dictionary, when creating a Series.
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)



calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
# ============= DataFrame =========== 
# A dataFrame is a tow-dimensional table with rows and columns. 

#creating a DataFrame

dataf = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(dataf)
print(df)
# Data fram in dictinory
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
df = pd.DataFrame(data)
print(df)
# Locate Row 
# As you can see form the result above, the DataFrame is Like a table with rows and columns.
 
#Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[0])
print(df.loc[[0,1]])

# Named Indexes
# With the index argument, you can name your own indexes.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)

# attributues


