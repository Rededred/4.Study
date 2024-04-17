import requests, time

url = 'https://api.binance.com/api/v3/ticker/price'

r = requests.get(url=url, params={'symbol': 'BTCUSDT'})
content = r.content
print(content)
print(type(content))

print(requests.get(url=url, params={'symbol': 'BTCRUB'}).content)

bitcoin_prices = []
for _ in range(30):
    response = requests.get(url=url, params = {'symbol':'BTCUSDT'})
    price = float(response.json()['price'])
    bitcoin_prices.append(price)
    time.sleep(0.5)
print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(bitcoin_prices))
print(min(bitcoin_prices))
