import time
# import matplotlib.pyplot as plt


def fib_bad(n):
    if n <= 1:
        return n
    return fib_bad(n-1) + fib_bad(n-2)

def fib(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
# fib = lambda n: (lambda f: f(n, [0, 1] + [0] * (n-1)))(lambda i, fib: fib[i] if i <= 1 else fib[i-1] + fib[i-2])
# надо бы ещё подумать над лямбдой

if __name__ == "__main__":
    ra = int(input())
    for n in range(ra+1):
        t1 = time.time()
        print(n, fib(n))
        t2 = time.time()
        print(f'Скорость хорошей функции: {t2-t1} секунд')
        print(n, fib_bad(n))
        t3 = time.time()
        print(f'Скорость плохой функции: {t3-t1} секунд')
        print()



