import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin
import datetime
import pytz
import csv 

yfin.pdr_override()

naive_datetime = datetime.datetime.now()
timezone = pytz.timezone('America/New_York')
aware_datetime = timezone.localize(naive_datetime)
# df = pdr.get_data_yahoo("SURE", start="2013-03-07", end="2013-03-08")
# # print(df)

# csv_file_path = 'data.csv'
# data = pd.read_csv(csv_file_path)
# print(data['1_year_later'][1])

def get_price(ticker, date):
    try:
        ny_timezone = pytz.timezone('America/New_York')
        start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        start_date = ny_timezone.localize(start_date)

        start_date_str = start_date.strftime('%Y-%m-%d')
        end_date = start_date + datetime.timedelta(days=1)
        end_date_str = end_date.strftime('%Y-%m-%d')
        
        df = pdr.get_data_yahoo(ticker, start=start_date_str, end=end_date_str, auto_adjust=True)
 
        return df['Close'][0]
    except Exception as e:
        print("--------------------------")
        print(ticker, "did not find...")
        print("--------------------------")
        return None

def to_next_business_day(date):
    dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    # Check if the given date is Saturday (5) or Sunday (6)
    while dt.weekday() in [5, 6]:  # loop to handle if consecutive days are weekends
        # Move to the previous day
        dt += datetime.timedelta(days=1)
    dt = str(dt)[:10]
    return dt

# Date format 
def date_next_day(date):
    start_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    end_date = (str(start_date + datetime.timedelta(days=3)))[:10]
    return end_date

def main():
    csv_file_path = "data.csv"
    data = pd.read_csv(csv_file_path)
    ranges = ["6month", "1_year_later", "2year"]
    # result = pd.DataFrame(data, columns=['Ticker', '6_month', '1_year', '2_years'])
    result = [['ticker', '6 months', '1 year', '2 years']]

    # anyways, there are 7241 lines...
    amount = 7242

    quoteClose = []
    for i in range(0, amount): # 7242
        ticker = data['ticker'][i]
        date = to_next_business_day(data['6month'][i])
        price = get_price(ticker, date)
        result.append([ticker, price])

    for i in range(0, amount): # 7242
        ticker = data['ticker'][i]
        date = to_next_business_day(data['1_year_later'][i])
        price = get_price(ticker, date)
        result[i + 1].append(price)
    
    for i in range(0, amount): # 7242
        ticker = data['ticker'][i]
        date = to_next_business_day(data['2year'][i])
        price = get_price(ticker, date)
        result[i + 1].append(price)
    
    with open("new_file.csv","w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(result)

    # print(quoteClose)

    

if __name__ == "__main__": 
    main()
