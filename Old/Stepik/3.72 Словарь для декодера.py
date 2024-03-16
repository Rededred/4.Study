a, b, c = input(), input(), {} # ввод переменных
for i in range(len(a)): # создание словаря зашиврованных значений
    k = a[len(c)]
    c[k] = b[i]


A = [str(i) for i in input()]
for i in range(len(A)):
    A[i] = c.get(str(A[i]))
A = ''.join(A) # кодирует инпут А

C = dict(zip(c.values(), c.keys()))

B = [str(i) for i in input()]
for i in range(len(B)):
    B[i] = C.get(str(B[i]))
B = ''.join(B) # декодирует инпут В

print(A)
print(B)