# a = int(input("больше или меньше 0"))


class Person:
    def __init__(self, new):
        self.name = new
        print("Создан человек с именем", self.name)
    def __del__(self):
        print("Удалён человек с именем", self.name)


tom = Person("TOM")

for i in range(50):
    print("rez:", tom.name, end=' | ')
print()