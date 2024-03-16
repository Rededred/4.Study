inf = open('3.44in.txt', 'r')
a = str(inf.readline())  # читает линию
inf.close()

# a = input()
len = len(a)
a = a+' '
n = int(0)
k = int(1)
result = ''
while True:
    result = a[n]
    if n==-1:
        break
    while a[n]==a[n+1]:
        k += 1
        n += 1
    print(str(result)+str(k), end='')
    k = 1
    n += 1
    if n ==len:
        break
