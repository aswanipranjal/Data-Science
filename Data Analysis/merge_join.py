# Merging and joining dataframes
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
					'Unemployment':[7, 8, 9, 6], 
					'Low_tier_HPI':[50, 52, 0, 53]},
					index=[2001, 2002, 2003, 2004])

# Merging kind of ignores the whole notion of index
# print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))

# Joining dataframes
df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)
# Now they are sharing index but no columns (which is important)

joined = df1.join(df3)
print(joined)