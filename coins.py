from coinmarketcap import Market

mkt = Market()
x=mkt.ticker("bitcoin", limit=3, convert="USD")
print('Bitcoin price in USD: ', x[0]['price_usd'])
print("Hola")
