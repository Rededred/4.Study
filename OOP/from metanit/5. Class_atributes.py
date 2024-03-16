class Person:
    default = "Undefined"

    def __init__(self, name, company, color):
        if name:
            self.name = name
            self.company = company
            self.color = color
        else:
            self.name, self.company, self.color = self.default, Person.default, self.default

    @staticmethod # позволяет использовать функцию по обращению к КЛАССУ, а не к МЕТОДАМ ОБЪЕКТА
    def printooo():
        print("oooooooooo")
        print("default = \"Undefined\"")

    def display_info(self):
        return self.name, self.company, self.color


tom = Person("TOM", "Face", "Red")
bob = Person('', '', '')

# Person.display_info()
Person.printooo()

print(tom.display_info())
print(bob.display_info())
