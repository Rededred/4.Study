class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, agggee):
        if 1 < agggee < 110:
            self.__age = agggee
        else:
            print("Wrong age!")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}\n"
              f"Age: {self.__age}")


tom = Person("TOM")

tom.display_info()  # Имя: Tom  Возраст: 1
tom.age = -3486  # Недопустимый возраст
print(tom.age)  # 1
tom.age = 36
tom.display_info()



