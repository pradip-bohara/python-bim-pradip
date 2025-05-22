import pandas as pd

# Sample DataFrames
data1 = {'key_column': ['A', 'B', 'C', 'D'],
         'value1': [1, 2, 3, 4]}
df1 = pd.DataFrame(data1)

data2 = {'key_column': ['A', 'B', 'E', 'F'],
         'value2': [5, 6, 7, 8]}
df2 = pd.DataFrame(data2)

# Merge df1 and df2 on 'key_column'
merged_df = pd.merge(df1, df2, on='key_column')
print(merged_df)

# Outer merge
outer_merged_df = pd.merge(df1, df2, on='key_column', how='outer')
print(outer_merged_df)

# Left merge
left_merged_df = pd.merge(df1, df2, on='key_column', how='left')
print(left_merged_df)

# Right merge
right_merged_df = pd.merge(df1, df2, on='key_column', how='right')
print(right_merged_df)



df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [85, 90, 78]})

# Merging on 'ID' (Common column)
merged_df = pd.merge(df1, df2, on='ID', how='inner')

print(merged_df)

df1 = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie']},
                   index=[1, 2, 3])

df2 = pd.DataFrame({'Score': [85, 90, 78]},
                   index=[2, 3, 4])

# Joining DataFrames
joined_df = df1.join(df2, how='inner')
print(joined_df)