inf = open('3.44in.txt', 'r')
a = str(inf.readline().split())  # читает линию
inf.close()

ouf = open('3.44out.txt', 'w+')  # first way записать
for i in range(len(a) - 1):
    if a[i].isdigit() and a[i - 1].isdigit():
        ouf.write(str(a[i - 2] * (int(str(a[i - 1])+str(a[i]))-int(a[i-1]))))
    elif a[i].isdigit():
        ouf.write(str(a[i - 1]) * int(a[i]))
ouf.close()
