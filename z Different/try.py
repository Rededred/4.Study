print(divmod(94, 7))  # возвращает целочисленный результат и остаток деления
print(abs(5/3))  # озвращает абсолютную величину???
print(5/3)
pto = 15
# print = pto
print(any([False, False, False, False]))
print(any([False, False, False, True]))

print(str(bin(50))[2:])  #возвращает число в бинарном виде
print(str(bin(50)))


class Person:
    def __init__(self, age, name):
        self.age = '123123'
        self.name = 'asdfasdf'
    def display_info(self):
        print(self.name, self.age)
andrey = Person(21, "Andrey")
tom = Person(23, "Tom")
tomy = Person(23, "Tom")
print(dir([Person]))  # выдаёт списком все (классы и методы) АТРИБУТЫ данного класса
                      # (видные и скрытые)
print(dir())  # выдаёт списком все классы и методы данного файла
print(callable([andrey]))  # False, так как нет метода __call__()
print(getattr(andrey, 'name'))  # получает именованный атрибут из объекта
                                # и меняет настоящий атрибут на изначальный
# print(getattr(Person, 'name')) # не работает, так как это класс
print(globals())  # возвращает все объекты (переменные) в компоненте
print(hasattr(andrey, 'name'), hasattr(andrey, 'nameeeeee'))

print(hash(andrey))
print(hash(tom))  # ????????????
print(hash(tomy))
# i = input()  # нельзя нажимать Ctrl-D, иначе ошибка
print(iter([1,2,3,4,5]))  # непонятный итератор
print(repr(tom))
setattr(tom, 'name', 'Больше не том')  # меняет значение атрибута name на новое
print(tom.name, tom.age)

print(andrey.__dict__)
print(tom.__dict__)
print(vars(tom))




