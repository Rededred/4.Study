from datetime import datetime as dt
from time import sleep

class Player:

    __NAME, __LVL, __HEALTH = "HERO", 1, 100
    __slots__ = ['__name', '__level', '__health', '__born']

    def __init__(self):
        self.__name = Player.__NAME
        self.__level = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def lvl(self):
        return self.__level, f'{dt.now() - self.__born}'

    @lvl.setter
    def lvl(self, numeric):
        self.__level += Player.__typesTest(numeric)
        if self.__level >= 100: self.__level = 100

    @classmethod
    def set_cls_field(cls, level=1, health=100):
        cls.__LVL = Player.__typesTest(level)
        cls.__HEALTH = Player.__typesTest(health)

    @staticmethod
    def __typesTest(self):
        if isinstance(self, int):
            return self
        else:
            raise TypeError ('Must be integer!')


# x = Player()
# print(x.lvl)
# x.lvl = 14
# print(x.lvl)
# # print(x.lvl())
# # x.lvl(2)
# # print(x.lvl())