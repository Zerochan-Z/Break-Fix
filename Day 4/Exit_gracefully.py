import yfinance as yf
import sys
import matplotlib.pyplot as plt

ticker = input('Enter the ticker symbol: ')
start_date = '2020-01-01'
end_date = '2021-01-01'

data = yf.download(ticker, start_date, end_date)

if data.empty:
    print(f'Invalid ticker : {ticker}')
    sys.exit(1)
else:
    print(f'{ticker} data downloaded successfully!')
    print(f'{ticker} chart is being plotted...')
    plt.plot(data.index,data['Close'],lw=2,label= ticker ,color='royalblue')
    plt.title(f'{ticker} Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()