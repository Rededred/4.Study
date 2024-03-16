from classN import Verification
from tkinter import Tk, Button

class V2(Verification):
    def __init__(self, login, password, age):
        # Verification.__init__(self, login, password)
        super().__init__(login, password)
        self.age = age
        self.__save()

    def __save(self):
        with open('user') as r:
            if f'{self.login, self.password, self.age}' + '\n' in r:
                print('almost exist!')
            else:
                print('Hello, New one!)')
                # Verification.save(self)
                super().save()

    def show(self):
        return self.login, self.password, self.age


x = V2('Kenny33', '123123123', 25)
# x.save() # так как уже добавлен в ИНИТ
# print(x.show())