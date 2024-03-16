class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __getitem__(self, prop):
        if prop == "name": return self.__name
        elif prop == "age": return self.__age
        return None


Andrey = Person("Andrey", 21)

print("Name:", Andrey["name"])
print("Age:", Andrey['age'])
print(Andrey[''])
