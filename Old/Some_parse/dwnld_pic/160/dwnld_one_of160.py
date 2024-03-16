import requests

for i in range(160):
    response = requests.get(url='https://parsinger.ru/img_download/img/ready/')
    with open(str(i)+'.png', 'wb') as file:
        file.write(response.content)