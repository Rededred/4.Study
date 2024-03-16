from modules import print_message as p_m
from modules import hello as h
# from modules import *
# Для импорта всей функциональности
# в глобальное пространство имен.
# Если * , то возможна коллизия имен функций!!
p_m("Hello world")
p_m(h)
print()

print(h)
h = 5
print(h)

