people = [
    ("Tom", 38, "Google"),
    ("Bob", 42, "Microsoft"),
    ("Sam", 29, "JetBrains")
]

for name, age, company in people:
    print(f"Name: {name},  Age: {age},  Company: {company}")

print("-----------------------------")
people = ['Tom', 'Bob', 'Sam']
for index, name in enumerate(people):
    print(f'{index}. {name}')

person =("Tom", 38, "Google")
name, _, company = person
print(name, _, company)

print("-----------------------------")
*numbers, = 1, 2, 3
print(numbers)

print("-----------------------------")
head, _, *tail, _, taile= [1, 2, 3, 4, 5]
print(head, tail, taile)
*head, tail = [1, 2, 3, 4, 5]
print(head, tail)

li, li2 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]], []
for i in li:
    li2 += [*i]
print(li2)

print("-----------------------------")
nums1 = [1, 2, 3]
nums2 = (4, 5, 6)
nums3 = *nums1, *nums2
# *nums3, = *nums1, *nums2  # то же самое
print(nums3)

dic1 = {"red":"красный", "blue":"синий"}
dic2 = {"green":"зеленый", "yellow":"желтый"}
dic3 = {**dic1, **dic2}
print(dic3)

print("-----------------------------")
def fun(*args):  # вместо *args может быть и *жопа, но первый вариант точно всем понятен, более формален
    print(args[0])
    print(args)

fun("Python", "C++", "Java", "C#")

def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result
print(sum(*[int(i) for i in range(4)]))
print(sum(*[int(i) for i in range(5)]))
print(sum(*[int(i) for i in range(6)]))

print("-----------------------------")
def fun(**kwargs):  # аналогично
    print(kwargs)
fun(name="Tom", age="38", company="Google")
fun(language="Python", version="3.11")

print("-----------------------------")
def fun(**kwargs):  # получение ключ - значения
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
fun(name='tom', age=38, company='Google')

print("----------------------------- Распаковка:")
def sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

numbers = (1, 2, 3, 4, 5)
print(sum(*numbers))

def print_person(name, age, company):
    print(f"Name: {name}, Age: {age}, Company: {company}")
# person("Tom", 38, "Google")
print_person(*person)

print("----------------------------- Сочетание параметров:")
def sum(num1, num2, *nums):
    result = num1 + num2
    for n in nums:
        result += n
    return result
print(sum(1,2,3))
print(sum(1,2,3,4,5))
