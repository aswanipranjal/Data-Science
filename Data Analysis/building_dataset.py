import quandl
import pandas as pd

api_key = 'VDxfKkzAm8MFL1fZsSat'
# The quandl module automatically assigns the index, here the 'Date' column is assigned as the index
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
print(df.head())

# Read fifty state codes through pandas, parsing a table on wikipedia
fifty_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# The link contains multiple tables, so fifty_states contains a list of dataframes. We need to figure out which is the one that we require
# print(fifty_states)
# We find that its the 0th element

# This is a dataframe
# print(fifty_states[0])

# This is a column
# print(fifty_states[0][0])

for abbv in fifty_states[0][0][1:]:
	print('FMAC/HPI_' + str(abbv))