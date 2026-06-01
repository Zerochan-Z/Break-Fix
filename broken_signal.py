'''Broken
import sys
import pandas as pd
import yfinance as yf
import os

file_name = sys.argv[1]
period = sys.argv[2]

if os.path.exists(file_name):
    os.remove(file_name)
    print(f'{file_name} is remved to keep data fresh.')

try:
    df = yf.download('AAPL', start= '2024-01-01',end = '2024-06-01')
    df.columns = df.columns.droplevel(1)
    df.reset_index(inplace=True)
    df = df[['Date','Close']].copy()
    df.to_csv(file_name,index = False)

    df['Close'] = df['Close']

    df['MA'] = 0
    for i in range(period, len(df)):
        df.loc[i, 'MA'] = df['Close'].iloc[i-period:i].mean()

    df['Signal'] = 'Hold'
    for i  in range(period,len(df)):
        if df.loc[i, 'Close'] > df.loc[i, 'MA']:
            df.loc[i, 'Signal'] = 'Buy'
        else:
            df.loc[i,'Signal'] = 'Sell'

    print(df[['Date','Close','MA','Signal']].head(15))

except Exception as e:
    print(f"Error: {e}")
'''

# Fixed

import sys
import pandas as pd
import yfinance as yf
import os

file_name = sys.argv[1]
period = int(sys.argv[2])

if os.path.exists(file_name):
    os.remove(file_name)
    print(f'{file_name} is remved to keep data fresh.')

try:
    df = yf.download('AAPL', start= '2024-01-01',end = '2024-06-01')
    df.columns = df.columns.droplevel(1)
    df.reset_index(inplace=True)
    df = df[['Date','Close']].copy()
    df.to_csv(file_name,index = False)

    df['MA'] = float('NaN')
    for i in range(period, len(df)):
        df.loc[i, 'MA'] = float(df['Close'].iloc[i-period:i].mean().round(4))

    df['Signal'] = 'Hold'
    for i  in range(period,len(df)):
        if df.loc[i, 'Close'] > df.loc[i, 'MA']:
            df.loc[i, 'Signal'] = 'Buy'
        elif abs(df.loc[i, 'Close'] - df.loc[i,'MA']) / df.loc[i,'MA'] <= 0.01:
            df.loc[i, 'Signal'] = 'Hold' 
        elif df.loc[i,'Close'] < df.loc[i,'MA']:
            df.loc[i,'Signal'] = 'Sell'

    print(df[['Date','Close','MA','Signal']].head(15))

except Exception as e:
    print(f"Error: {e}")