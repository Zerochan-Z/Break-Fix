import pandas as pd
import numpy as np


df = pd.read_csv('data1.csv',header=None, names=['name', 'salary'])
print('Columns in file: ', list(df.columns))

try:
    print(df[['name','age']])

except KeyError:
    print('Available columns: ', list(df.columns))
    print('\nStarting to generating random ages for each person...')
    df['age'] = np.random.randint(20, 60, size=len(df))
    print(df[['name', 'age']])
    