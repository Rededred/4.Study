# class Person:
#     def __init__(self, name):
#         self.name = name
#         # self.age = 1
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 1<age<110:
#             self.__age = age
#         else:
#             print('Недопустимо')
#
#     def display_info(self):
#         print(f'Имя: {self.name}\tВозраст: {self.age}')
#
# print('Введите свои имя и возраст')
#
# andrew = Person('Andrey')
# andrew.name = 'Andrew'
# andrew.age = 19
# andrew.display_info()

class PersonAgeExeption(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f'Недопустимое значение: {self.age}.'\
               '\n'\
               f'Возраст должени быть в диапазоне от {self.minage} до {self.maxage}'

class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeExeption(age, minage, maxage)

    def display_info(self):
        print(f'Имя: {self.__name} Возраст: {self.__age}')

try:
    tom = Person('Tom', 37)
    tom.display_info()
    fo = Person(4, 4)
    fo.display_info()
    bob = Person('Bob', 115)
    bob.display_info()


except PersonAgeExeption as e:
    print(e)

