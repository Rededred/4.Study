import requests

r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')

while True:
    if not r.text.startswith('We'):
        print(r.text)
        r = requests.get('https://stepik.org/media/attachments/course67/3.6.3/'+r.text)
        continue
    else:
        print(r.text)
        break
