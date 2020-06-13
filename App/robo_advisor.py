# Info Inputs

import requests
import json
import csv
import os
from dotenv import load_dotenv
import re

load_dotenv()

#Specify Input Stock Ticker
# Input Stock Ticker
# Input the the value you believe the stock is worth based on your research

while True:
    ticker = str(input("Input Stock Ticker: "))
    #< if not
    if not re.match("^[A-Z]*$", ticker):
        print("Error! Try Again, Only Capital Letters (A-Z) Allowed")
    elif len(ticker) > 5:
        print("Error! Try Again, Maximum 5 Letters Allowed")
    else:
        break

while True:
    try:
        value = float(input('Input Stock Expected Value: '))
    except ValueError:
        print("Error! Please Enter a Valid Stock Price")
    else:
        break
            

api_key = os.environ.get("alpha_vantage_api_key")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}"
response = requests.get(request_url)

parsed_response = json.loads(response.text)

#latest dates

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0]

latest_close = float(tsd[latest_day]["4. close"])
latest_close_usd = float(latest_close)
latest_close_usd = "${0:.2f}".format(latest_close_usd)

# Maximum of all high prices
high_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))


recent_high = max(high_prices)
recent_high_usd = float(recent_high)
recent_high_usd = "${0:.2f}".format(recent_high_usd)

# Minimum of all low prices
low_prices = []

for date in dates:
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))


recent_low = min(low_prices)
recent_low_usd = float(recent_low)
recent_low_usd = "${0:.2f}".format(recent_low_usd)

#Write to CSV

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],

    })

# Specify Time/Date
import datetime
e= datetime.datetime.now()
date_time = e.strftime("%I:%M %p %m/%d/%Y")


print("-------------------------")
print(f"SELECTED SYMBOL: {ticker}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {date_time}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {latest_close_usd}")
print(f"RECENT HIGH: {recent_high_usd}")
print(f"RECENT LOW: {recent_low_usd}")
print("-------------------------")
print("RECOMMENDATION: ")
if value > latest_close:
        print ("BUY!")
elif value < latest_close:
        print ("DO NOT BUY!")
print("RECOMMENDATION REASON:")
if value > latest_close:
        print ("Stock is Undervalued Compared to Your Valuation, You Should Buy!")
elif value < latest_close:
        print ("Stock is Overvalued Compared to Your Valuation, You Should Not Buy")
print("-------------------------")
print(f"WRITING DATA TO {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
