n, m, k = (int(i) for i in input().split())  # n - row, m - column, k - mines

a = [[0 for j in range(m)] for i in range(n)]
# print(a)

for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    # row, col = (int(i) - 1 for i in random.randint(m).split())
    a[row][col] = -1
# print(a)

for i in range(n):  # обход каждой строки
    for j in range(m):  # обход по ячейкам строки a[i]
        if a[i][j] == -1:
            continue  # т.е т.к в этой ячеке мина, пропускаем её

        for di in range(-1, 2):  # проверяем слева и справа, 2 невключительно))
            for dj in range(-1, 2):  # проверяем сверху и снизу от текущей ячейки
                ai = i + di
                aj = j + dj
                # a[ai][aj] - Проверяемая ячейка вокруг текущей

                if 0 <= ai < n and 0 <= aj < m:  # не выходит ли за пределы n*m
                    if a[ai][aj] == -1:
                        a[i][j] += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == - 1:
            print('*', end='  ')  # тут мина
        elif a[i][j] == 0:
            print('.', end='  ')  # тут пусто
        else:
            print(a[i][j], end='  ')  # тут пусто, но рядом есть мины
    print()  # переход на следующий ряд (строчку)
