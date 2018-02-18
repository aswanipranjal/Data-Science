# Concatenating and appending dataframes
import pandas as pd

df1 = pd.DataFrame({'HPI':[80, 85, 88, 85],
					'Int_rate':[2, 3, 2, 2], 
					'US_GDP_Thousands':[50, 55, 65, 55]},
					index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80, 85, 88, 85],
					'Int_rate':[2, 3, 2, 2],
					'US_GDP_Thousands':[50, 55, 65, 55]},
					index=[2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80, 85, 88, 85],
					'Int_rate':[2, 3, 2, 2], 
					'Low_tier_HPI':[50, 52, 0, 53]},
					index=[2001, 2002, 2003, 2004])

# concatenate new rows at the end
concat = pd.concat([df1, df2])
print(concat)

# Concat always adds to the bottom
# If we concatenate df1, df2 and df3, well... weird things will happen... duplicate row entries, NaN's, etc
concat = pd.concat([df1, df2, df3])
print(concat)

# Append adds to the end
# df4 = df1.append(df2)
# print(df4)

# Pandas is not a Database management system. It wasn't built to make dynamic tables and databases. It was built for analysis
# and manipulation of data, so adding a new entry is not as efficient and is a bit of a chore
s = pd.Series([80, 2, 50], index=['HPI', 'Int_rate', 'US_GDP_Thousands'])

df4 = df1.append(s, ignore_index=True)
print(df4)