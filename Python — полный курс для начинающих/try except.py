import requests, time

bitcoin_prices = []
url = 'https://api.binance.com/api/v3/ticker/price'

try:
    for _ in range(30):
        response = requests.get(url=url, params = {'symbol':'BTCUSDT'})
        price = float(response.json()['price'])
        bitcoin_prices.append(price)
        time.sleep(0.5)
except requests.exceptions.ConnectionError as e:
    print(f"Нету интернету: {e}")
print(bitcoin_prices)
