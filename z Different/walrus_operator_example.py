# неудобно
def dump1():
    value = input('Please enter something: ')
    while value != '':
        print('Nice')
        value = input('Please enter something: ')

# удобно из-за моржёвого оператора
def dump2():
    while (value := input('Please enter something: ') != ''):
        print('Nice!')


def cube(num):
    return num**3
num_list = [1, 2, 3, 4, 5]
# res = [cube(x) for x in num_list if cube(x) < 20]
res = [y for x in num_list if (y := cube(x)) < 20]
print(res)
# последний способ эффективней,
# так как функция cube вызывается лишь 1 раз
