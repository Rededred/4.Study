class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __contains__(self, prop):
        if prop == "name" or prop == "age": return True



andrey = Person("Andrey", 21)
andrey2 = Person("Andrey", 21)
print(andrey)
print(andrey2)
print("name" in andrey)
print("id" in andrey)