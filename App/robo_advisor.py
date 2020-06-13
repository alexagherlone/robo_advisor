# Info Inputs

import requests
import json

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=GU0UCNTUW6P7OZZC"
response = requests.get(request_url)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]
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

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {latest_close_usd}")
print(f"RECENT HIGH: {recent_high_usd}")
print(f"RECENT LOW: {recent_low_usd}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
