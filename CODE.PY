import pandas as pd
import numpy as np

df = pd.read_csv('C:\Users\sahib\Downloads\demo.csv')

# shape and data types of the data
print(df.shape)
print(df.dtypes)
print(df.dtypes.to_string())
