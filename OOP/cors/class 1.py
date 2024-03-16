

class Purse:
    def __init__(self, currency, name = 'unknown'):
        if currency not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = currency
        self.name = name

    def top_up_balance(self, howmuch):
        self.__money = self.__money + howmuch

    def top_down_balance(self, howmuch):
        if self.__money - howmuch < 0:
            print('Нет денег')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmuch
        return howmuch

    def info(self):
        print(self.__money)
        # return self.money


    def __del__(self):
        print('Кошелёк удален')
        # return self.money


x = Purse('USD')
y = Purse('EUR', 'Bill')
x.top_up_balance(100)
y.top_up_balance(100)
x.top_up_balance(y.top_down_balance(15))
x.info()
y.info()

# del x
# x.money = -200
# x.money
