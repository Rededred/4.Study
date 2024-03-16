chose = input('Вывести только простые чила? (впишите да или нет) ')

N = int(input("Введите верхнее число: ")) + 1
A = [True] * (N)

A[0] = A[1] = False


def body(A: list, N: int):
    """
    Отображает и простые и составные числа
    """
    for k in range(2, N):
        for m in range(2 * k, N, k):
            A[m] = False
    for k in range(N):
        print(k, "- простое" if A[k] else "- составное")


def body_special(A: list, N: int):
    """
    Отображает только простые
    """
    for k in range(2, N):
        for m in range(2 * k, N, k):
            A[m] = False
    for k in range(N):
        if A[k]:
            print(k)


# def final():


if __name__ == "__main__":
    if chose != ("да" or "нет"):
        print("не понял")
    if chose == "да":
        body_special(A, N)
    elif chose == "нет":
        body(A, N)
    # print(globals())
