from dataclasses import dataclass

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

tom = Person("Tom", 38)
print(f'Name: {tom.name}   Age: {tom.age}')

@dataclass
class Person:
    name: str
    age: int = 18

    def say_hello(self):
        print(f"{self.name} says hello")

tom = Person("Tom", 38)
tom.say_hello()
print(f'Name: {tom.name}   Age: {tom.age}')
bob = Person("BOB")
print(bob)
bob.say_hello()
print(input().isdigit())
