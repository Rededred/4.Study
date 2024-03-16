# Напишите программу, которая принимает на вход список чисел
# в одной строке и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза.

a, c = [str(i) for i in input().split()], []
for i in a:
    if i not in c and a.count(i) > 1:
        c.append(i)
        print(i, end=' ')

# Ниже моё - выше ОПТИМАЛЬНОЕ

# a = input().split()
# a = sorted(a)
# for j in range(10):
#     print(j, end=' ')
# b = len(a)
# n = int(0)
# result = ''
# while n < b:
#     result = a[n]
#     if result == a[-1]:
#         if a[-1] == a[2]:
#             print(str(result), end=' ')
#             break
#         else:
#             break
#     if a[n] == a[n + 1]:
#         while a[n] == a[n + 1]:
#             n += 1
#         print(str(result), end=' ')
#     elif a[n] != a[n + 1]:
#         n += 1
#     else:
#         print(str(result), end=' ')
