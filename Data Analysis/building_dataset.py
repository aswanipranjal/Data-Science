import quandl
import pandas as pd

api_key = 'VDxfKkzAm8MFL1fZsSat'
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
print(df.head())