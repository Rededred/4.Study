import requests
from tqdm import tqdm

for i in tqdm(range(1, 501)):
    url = f'https://parsinger.ru/task/1/{i}.html'
    response = requests.get(url)
    try:
        n = 1/(response.status_code - 404)
        print(response.status_code, response.url, response.text)
        break
    except:
         continue


# import requests
#
# url = 'http://parsinger.ru/task/1/'
#
# try:
#     for n in range(350, 1, -1):
#         va = 1 / (requests.get(url + str(n) + '.html').status_code - 200)
#         print(n)
# except:
#     print(requests.get(url + str(n) + '.html').text)



# for n in range(1, 501):
#     if requests.get(url + str(n) + '.html').status_code == 200:
#         print(n, "YES")
#     else:
#         print(n)



# for n in range(350, 1, -1):
#     resp = requests.get(url + str(n) + '.html')
#     code = resp.status_code
#     try:
#          va = 1 / (code - 404)
#          print(n, "YES")
#     except:
#          print(n)



# try:
#     for n in range(350, 1, -1):
#         va = 1 / (requests.get(url + str(n) + '.html').status_code - 200)
#         print(n)
# except:
#     print(requests.get(url + str(n) + '.html').text)
