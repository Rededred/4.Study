from fake_useragent import UserAgent
import requests


url = 'https://httpbin.org/user-agent'
ua = UserAgent()

for _ in range(10):
    fake_ua = {'user-agent': ua.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)