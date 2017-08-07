import pandas as pd
df = pd.read_csv('C:\\Users\\Aman Deep Singh\\Documents\\Python\\Data Science\\Data Analysis\\housing77006.csv')
print(df.head())

df.set_index('Date', inplace=True)
df.to_csv('C:\\Users\\Aman Deep Singh\\Documents\\Python\\Data Science\\Data Analysis\\housing77006_v2.csv')