import pandas as pd
df = pd.read_csv('data.csv')

# Viewing the Data 
""" One of the most used mehtod for getting a quick
 overview of the DataFrame, is the head() method
    The head() method returns the headers and specified 
    number of rows starting form the top.
    """
print(df.head(10))


""" There is also a tail() method for viewing the 
last rows of the DataFrame.
The tail() method returns the headers and a specified 
number of rows, starting from the bottom."""

print(df.tail())
# print(df.tail())
# print("\n")
# print(df.head)

# print(df.to_string())  # to print the entire DataFrame.

# ======= max-rows The number of rows returned is defined in Pandas option setting

# pd.options.display.max_rows = 9

# df = pd.read_csv('data.csv')

# print(df) 

# Attributes of a DataFrame
# Number of rows and columns
print(df.shape)

# Column names
print(df.columns)

# Data types of each column
print(df.dtypes)

# Index information
print(df.index)

# ===== Working with Missing Data =========== 
# Sometimes, datasets contain missing values. Pandas provides methods to handle them. 

data = {
    'Name': ['Alice', 'Bob', None],
    'Age': [25, None, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)
print(df.isnull())

# Indexing, Slicing, and Subsetting
# access specific columns or rows in a DataFrame.
# Indexing 
print(df['Name']) # Access a single column

#Slicing Rows 
print(df[0:2]) #Get first tow rows

# Subsetting (Selecting Multiple Columns)
print(df[['Name', 'Age']])


# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, None, 22, 29],
        'City': ['New York', 'Los Angeles', None, 'Chicago']}

df = pd.DataFrame(data)

# Detect missing values
print(df.isnull())

# Fill missing values with a specified value
df_filled = df.fillna(value={'Age': 25, 'City': 'Unknown'})
print(df_filled)

# Remove rows with any missing values
df_dropped = df.dropna()
print(df_dropped)

# Remove columns with any missing values
df_dropped_columns = df.dropna(axis=1)
print(df_dropped_columns)

# Remove rows with all missing values
df_dropped_all = df.dropna(how='all')
print(df_dropped_all)

#indexing and Slicing
# Indexing
print(df['Name']) # Access a single
# Slicing Rows
print(df[0:2]) # Get first two rows
# Subsetting (Selecting Multiple Columns)
print(df[['Name', 'Age']])
# Selecting Rows Based on Conditions
print(df[df['Age'] > 25])
# Selecting Rows Based on Multiple Conditions
print(df[(df['Age'] > 25) & (df['City'] == 'Chicago')])

