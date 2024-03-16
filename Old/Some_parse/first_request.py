import requests


response = requests.get(url='https://httpbin.org/')
print(type(response))


response = requests.get(url='https://httpbin.org/user-agent')
print(response.text)
