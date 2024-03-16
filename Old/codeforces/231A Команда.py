num = int(input())

n = 0
result = 0
while n < num:
    k = 0
    for i in input().split():
        k += int(i)
    if k >=2:
        result += 1
    n += 1

print(result)

