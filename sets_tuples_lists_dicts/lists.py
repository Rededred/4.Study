# list[start:end:step]

print([5]*6)
print(["Andrey"]*7)
students = ["bob", "sam"] * 2
students.append('sadfsdf')
print(students)
print("----------------------")

people = ["Tom", "Sam", "Bob", "Tom", "Bob", "Sam1"]
pep = people.copy()
people.append("Alice")
pep.extend(['dod', "tot", 'rod', 'code'])
print(people.pop(people.index("Sam1")))  #удаляет и возвращает!
print(people.count("Bob"))
# print(people.pop(-1))  #удаляет и возвращает!
print(sorted(pep))
print(min(pep), max(pep))
people.sort()
people.reverse()
people.insert(people.index("Sam"), 'asdf')
people.remove("Sam")
# people.clear()
print(people)
del pep[pep.index("dod")]  #только так или по индексу!
print(pep)
print("-----------------------------")
for i in range(len(people)):
    if i%2==0:
        people[i] = 'не подходит'
    print(people[i])

try:
    tom, bob, sam = people
    print(people)
except ValueError:
    print("-----------------------")
    print("NO")

nums = [10, 20, 30, 40, 50]
nums[1:4] = [11, 22]
print(nums)
print("---------------------------------------")

people = ["Tom", "bob", "alice", "Sam", "Bill"]
people.sort(key=str.lower)
print(people)
people.sort(key=str.upper)  #то же самое, так как лоит или аперит всё
print(people)
print("---------------------------------------")

people = ["Tom", "bob", "alice", "Sam", "Bill"]
print(sorted(people, key=str.lower))
print("---------------------------------------")

# ФИЛЬТРАЦИЯ СПИСКА filter(function, inter_object)
numbers = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]
def condition(number): return number > 1
for n in filter(condition, numbers): print(n, end=' ')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
print()
print("---------------------------------------")
people = [Person("Tom", 38), Person("Kate", 21), Person("Bob", 42),
          Person("Fred", 35), Person("Sam", 25), Person("BadMan", 37)]
# фильтрация элементов, у которых возраст <=35
view = filter(lambda p: p.age <= 35, people)
for person in view:
    print(f"Name: {person.name}  Age: {person.age}")
print("---------------------------------------")

# ПРОЕКЦИЯ СПИСКА (проход через него через map)
numbers = [1, 2, 3, 4, 5]
# def squer(number): return number*number
# result = map(squer, numbers)
# for n in result: print(n, end=' ')
for n in map(lambda k: k*k, numbers): print(n, end=' ')
print()
print("---------------------------------------")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Tom", 38), Person("Kate", 31), Person("Bob", 42),
          Person("Alice", 34),  Person("Sam", 25)]

for person in map(lambda p: [p.name, p.age], people):
    print(*person)
print("---------------------------------------")




