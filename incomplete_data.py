import pandas as pd

df = pd.read_csv('incomplete_data.csv',index_col='Date')
print('Original data: ')
print(df)
print('\nMissing Values per row: ')
print(df.isnull().sum(axis=1))

returns_clean=df.dropna()
returns = returns_clean.pct_change()

correlation=returns_clean['AAPL'].corr(returns_clean['TSLA'])

print(f'Correlation: {correlation:.4f}')
print(f'Rows used: {len(returns_clean)}')
print(f'Original rows: {len(returns)}')

