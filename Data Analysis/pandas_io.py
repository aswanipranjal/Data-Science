import pandas as pd
# index_col=0 sets the first column as the index column
df = pd.read_csv('C:\\Users\\Aman Deep Singh\\Documents\\Python\\Data Science\\Data Analysis\\housing77006.csv', index_col=0)
print(df.head())

# df.set_index('Date', inplace=True)
# df.to_csv('C:\\Users\\Aman Deep Singh\\Documents\\Python\\Data Science\\Data Analysis\\housing77006_v2.csv')
# Even though we defined the 'Date' column to be the index, when we import it again, nothing changes, so we 
# can define the index column inside the read_csv function just as we are importing the dataframe