import requests

url = 'http://httpbin.org/ip'
proxy = {
    'http': 'http://39.107.33.254:8090', #random proxy
    'https': 'http://39.107.33.254:8090',

}

response = requests.get(url=url, proxies=proxy)
print(response.json())

