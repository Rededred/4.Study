import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.84 Safari/537.36 ZHOu',
}

response = requests.get(url='https://httpbin.org/user-agent', headers=headers)
print(response.text)
