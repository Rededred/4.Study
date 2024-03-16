d = {}
k = 0
while k < 100:
    a = input().split()
    d.update({a[0]: a[1]})
    k += 1
    if k // 5 == 0:
        print()

print(d)

