class some_new:
    def __init__(self, integer, tupla):
        self.inte = integer
        self.tup = tuple(tupla)

    @staticmethod
    def multiply(integer, tupla):
        for i in tupla:
            print(i * integer)


exhibition = some_new(3, [1, 2, 3, 4, 5, 6])
exhibition.multiply(exhibition.inte, exhibition.tup)
