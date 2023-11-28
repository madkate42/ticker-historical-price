import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
import pytz
import csv 
yf.pdr_override()
naive_datetime = datetime.datetime.now()
timezone = pytz.timezone('America/New_York')
aware_datetime = timezone.localize(naive_datetime)

def get_data(ticker, date):
    try:
        ny_timezone = pytz.timezone('America/New_York')
        start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        start_date = ny_timezone.localize(start_date)

        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date = start_date + datetime.timedelta(days=1)
        end_date_str = end_date.strftime('%Y-%m-%d')
        
        # df = pdr.get_quote_yahoo(ticker, start=start_date_str, end=end_date_str, auto_adjust=True)
        # df = yfin.get_quote_yahoo(ticker)
 
        return df
    
    except Exception as e:
        print("--------------------------")
        print(ticker, "did not find...")
        print("--------------------------")
        return None
    
def get_market_cap(ticker):
    try:
        tick = yf.Ticker(ticker)
        market_cap = tick.info["marketCap"]
        return market_cap 
    except Exception as e:
        print("whatever")
        return None

# print(get_data('MSFT', "2023-11-20"))

# Create a Ticker object for the stock you're interested in
# ticker_symbol = "AAPL"  # Replace with the stock symbol you want to fetch data for
# ticker = yf.Ticker(ticker_symbol)

# Get the market cap data
# market_cap = ticker.info["marketCap"]
# print(f"Market Cap for {ticker_symbol}: {market_cap}")

market_caps = []
data = list(csv.reader(open("2year_data.csv")))
for i in range(1, 3553): # 3553
    stock = str(data[i][4])
    mc = get_market_cap(stock)
    data[i].append(mc)
    print(stock, "done. index", i)

with open("fuckeverything.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data)
