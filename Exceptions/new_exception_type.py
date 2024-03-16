class PersonAgeException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"\nНедопустимое значение: {self.age}." \
               f"\nВозраст должен быть в диапазоне от {self.minage} до {self.maxage}!"


class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(age, minage, maxage)

    def display_info(self):
        print(f"Name is: {self.__name}\nAge is: {self.__age}")


try:
    andrey = Person("Andrey", 21)
    andrey.display_info()

    bob = Person("BOB", -27)
    bob.display_info()
except PersonAgeException as e:
    print(e)