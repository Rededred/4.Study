# a, b = [int(i) for i in input().split()]

nm = input().split()
n = input().split()

i = 0
while i < len(n):
    l = input().split()

    o = 0
    k = 0
    while o <= (abs(int(l[0])-int(l[1]))):

        if l[0] > l[1]:
            k += int(l[0+o])
        else:
            n = list(reversed(n))

        o += 1

    i += 1

'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
l = [0] + [max(0, a[i] - a[i + 1]) for i in range(n - 1)]
r = [0] + [max(0, a[i] - a[i - 1]) for i in range(1, n)]
for i in range(n - 1):
    l[i + 1] += l[i]
    r[i + 1] += r[i]
for _ in range(m):
    s, t = map(int, input().split())
    if s < t:
        print(l[t - 1] - l[s - 1])
    else:
        print(r[s - 1] - r[t - 1])
'''
