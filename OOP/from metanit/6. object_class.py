class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        # return f"Name: {self.name} \nAge: {self.age}"
        return self.__str__()  #МОЖНО ТАК

    def __str__(self):
        return f"Name: {self.name} \nAge: {self.age}\n"


tom = Person("TOM", 23)
print(tom)
print(tom.display_info())
