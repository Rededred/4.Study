a, b = [int(i) for i in input().split()]  # задаем диапазон через пробел
print(sum([i for i in range(a,b+1) if i % 2 == 1]))

# or

a, b = (int(i) for i in input().split())
s = 0
if a%2 ==0:
    a+=1
for i in range(a, b+1, 2):
    s+=i
print(s)

# Вывод:
# 1 2
# 1
# 1 2
# 1