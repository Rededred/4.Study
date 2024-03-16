class Person:
    ns = "not stated"

    def __init__(self, name=ns, age=ns):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"Имя: {self.__name}\n"
              f"Возраст: {self.__age}")


incognito = Person()
def di():
    incognito.display_info()


di()
incognito.name = "Vasiliy"
incognito.age = 123
print(incognito.name)
di()
