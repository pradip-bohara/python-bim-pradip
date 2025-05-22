import pandas as pd

df = pd.read_csv('somdata.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())
