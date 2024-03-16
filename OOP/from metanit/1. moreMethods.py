class outoPuto:
    def __init__(self, mes):
        self.message = mes

    def say(self):
        print(self.message+" ||| Oh YES!")

    def Nosay(self):
        print("||| Не буду выводить сообщение:", self.message)


try_ = outoPuto("\"Что-то я да пишу тут\"")
try_.say()
try_.Nosay()
