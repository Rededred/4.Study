a = [int(i) for i in input().split()]

ma = a[0]
mi = a[0]

for x in a:
    if ma<x:
        ma = x
print('Максимум:', ma)

for x in a:
    if mi>x:
        mi = x
print('Минимум:', mi)

