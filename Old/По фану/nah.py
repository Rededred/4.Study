import time


class Some():
    def __init__(self, name):
        self.name = name
        print(f'Создан объект Some под названием {self.name}')

    def say(self, saying):
        print(saying)

    def sayN(self, repit):
        N = 3
        k = 0
        while k < N:
            time.sleep(0.5)
            print(repit)
            k += 1
        time.sleep(0.5)
        print('----------------------------------------------------------------------')
        time.sleep(0.5)
        print('Успешно выполнено!')

    def nah(self):
        nah = 'Пшёл на хуй, padla :D'
        for i in nah:
            if i == ' ':
                print(i, end='')
            else:
                print(i, end='')
                time.sleep(0.3)


f = Some('F')
f.sayN('Nigga')
print()
f.nah()
print()
