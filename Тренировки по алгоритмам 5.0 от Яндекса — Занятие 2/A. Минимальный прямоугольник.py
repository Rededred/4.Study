inp = [[int(i) for i in input().split()] for i in range(int(input()))]

maxes =max([int(i[0]) for i in inp]),  max([int(i[1]) for i in inp])
mins =min([int(i[0]) for i in inp]),  min([int(i[1]) for i in inp])

print(*mins, *maxes)

"""
На клетчатой плоскости закрашено K клеток.
Требуется найти минимальный по площади прямоугольник,
со сторонами, параллельными линиям сетки,
покрывающий все закрашенные клетки.
Ввод:
4
1 3
3 1
3 5
6 3
Вывод:
1 1 6 5
"""