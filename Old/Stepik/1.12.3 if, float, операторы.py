a = float(input())
b = float(input())
op = str(input())

if op == 'pow':
    print(a**b)
elif op == 'div':
    if b != 0:
        print(a//b)
    else:
        print('Деление на 0!')
elif op == 'mod':
    if b != 0:
        print(a%b)
    else:
        print('Деление на 0!')
elif op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    if b != 0:
        print(a/b)
    else:
        print('Деление на 0!')
else:
    pass
