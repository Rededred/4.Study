b = list(map(int, input().split()))
a=0
for i in b:
    a+=i
print(a)
# ниже шикарное решение
print(sum(int(i) for i in input().split()))