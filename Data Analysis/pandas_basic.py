# Pandas is like Excel for Python
# Pandas is easier than Python + Numpy
# A dataframe is like a Python dictionary
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day':[1, 2, 3, 4, 5, 6],
			'Visitors':[43, 53, 34, 45, 64, 34],
			'Bounce_Rate':[65, 72, 62, 64, 54, 66]}

# Create DataFrame
df = pd.DataFrame(web_stats)
# We print the head to be sure if the dataframe has been created
print(df.head())