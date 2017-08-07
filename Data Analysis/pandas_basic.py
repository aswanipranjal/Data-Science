# Pandas is like Excel for Python
# Pandas is easier than Python + Numpy
# A dataframe is like a Python dictionary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1, 2, 3, 4, 5, 6],
			'Visitors':[43, 53, 34, 45, 64, 34],
			'Bounce_Rate':[65, 72, 62, 64, 54, 66]}

# Create DataFrame
df = pd.DataFrame(web_stats)
# We print the head to be sure if the dataframe has been created
# An index is automatically generated
# print(df.head())
# Prints last 5 columns
# print(df.tail())
# Prints last 2 columns
# print(df.tail(2))

# To set an index
# This returns a new dataframe. Doesn't modify the original dataframe
# print(df.set_index('Day'))
# print(df.head())

# To workaround this, one way is
# df = df.set_index('Day')
# print(df.head())

# A better way is
# df.set_index('Day', inplace=True)
# print(df.head())

# To get a specific column
# Used with datasets which have column names with spaces
# print(df['Visitors'])

# Another way to do the same thing
# Used more often
# print(df.Visitors)

# To print specific columns
# print(df[['Visitors', 'Bounce_Rate']])

# To convert to a list
# print(df.Visitors.tolist())

# Even though multi-dimensional lists are valid, converting multiple columns to n-dimensional lists is not allowed
# Use numpy arrays instead
# print(np.array(df[['Visitors', 'Bounce_Rate']]))

# df2 = pd.DataFrame(np.array(df[['Visitors', 'Bounce_Rate']]))
# print(df2)