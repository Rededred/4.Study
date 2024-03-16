n = int(input())
a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])

import math
x = int(input())
print(*[int(1/2 + math.sqrt(2 * n)) for n in range(1, x + 1)])

# Андрюша, ты тормозишь, ПРЕКРАЩАЙ
# похожее на то, что ниже!

a = [i for i in range(1, int(input())+1)]
b = []
n = 1
k = 0

while len(b) <= len(a):
    if len(a) == 1:
        b = [1]
        break
    if len(a) == 2:
        b = [1, 2]
        break
    if len(a) == 3:
        b = [1, 2, 2]
        break
    if a[n] == n+1:
        b += [a[k]]*n
        n += 1
        k += 1
b = b[:len(a)]
print(*b)