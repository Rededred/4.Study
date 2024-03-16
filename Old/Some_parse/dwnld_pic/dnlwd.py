import requests

response = requests.get(url='http://httpbin.org/image/jpeg')
with open('image.jpeg', 'wb') as file:
    file.write(response.content)