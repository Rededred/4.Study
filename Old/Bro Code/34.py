import shutil
import time
import os


# with open('SomeFile.txt', 'a') as sm:
#     sm.write('Some text is here\n')
i = 0
while True:
    new = f'{time.time()}.txt'
    shutil.copyfile('SomeFile.txt', 'scam\\' + new)
    i += 1
    if i == 10:
        break
# try:
#     os.mkdir('scam')
#     i = 0
#     while True:
#         new = f'{time.time()}.txt'
#         shutil.copyfile('SomeFile.txt', 'scam\\'+new)
#         i += 1
#         if i == 10:
#             break
# except FileExistsError:
#     shutil.rmtree('scam')
