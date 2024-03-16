class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name is: {self.__name}")

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"Company is: {self.company}")

    def work(self):
        print(f"{self.name} works")


tom = Employee("Tommy", "Jeans")
tom.display_info()
print(Employee.mro())




# print("class".mro())
# print(WorkingStudent.__mro__)