# -*- coding: cp1251 -*-
class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f'Недопустимое значение: {self.age}. '\
               f'Возраст должен быть в диапазоне от {self.minage} до {self.maxage}!'



class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f'Имя:{self.__name}\tВозраст: {self.__age}')


try:
    tom = Person('Tom', 37)
    tom.display_info()

    bob = Person('Bob', -0xf)
    bob.display_info()
except PersonAgeException as e:
    print(e)
