import pandas as pd

df = pd.read_csv('somdata.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d', errors='coerce')

print(df.to_string())



data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 29],
        'City': ['New York', 'Los Angeles', 'San Francisco', 'Chicago']}
df = pd.DataFrame(data)

# Write data to a CSV file
df.to_csv('output.csv', index=False)