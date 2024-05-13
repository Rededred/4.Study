class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        return hash((self.name, self.age))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.name == other.name and self.age == other.age

person1 = Person("John", 30)
person2 = Person("John", 30)
person3 = Person("Jane", 25)

print(hash(person1))  # Вывод: 5736431
print(hash(person2))  # Вывод: 5736431
print(hash(person3))  # Вывод: 5736432


print(person1 == person2)  # Вывод: True
print(person1 == person3)  # Вывод: False

a=0
print(person1 == a)  # Так как переменная не имплементированна в класс