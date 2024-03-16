import os.path

inf = open('3.44in.txt', 'r') # first way прочитать
s1 = inf.readline() # читает линию
s2 = inf.readline()
inf.close()

with open('text') as inf: # second way
    s1 = inf.readline()
    s2 = inf.readline()
    # файл закрывается сам


s = inf.readline().strip() # оголить от перевода строки, разрыва строки

# import os
os.path.join('3.4 Файловый ввод', 'dirname', 'filename.txt') # позволяет создать путь к файлу (/для линукса и мака, \для виндовс)
'./dirname/filename.txt'

with open('input.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)

ouf = open('3.44in.txt', 'w') # first way записать
ouf.write('Какой-то тексекс)\n')
ouf.write(str(25))
ouf.close()

with open('3.44out.txt', 'w') as ouf:
    ouf.write('Какой-то текст\n')
    ouf.write(str(25))