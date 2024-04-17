def fib_bad(n):
    if n <= 1:
        return n
    return fib_bad(n-1) + fib_bad(n-2)

def fib(n):
    fib = [0, 1] + [0] * (n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


if __name__ == "__main__":
    for n in range(44):
        print(n, fib(n))
        print(n, fib_bad(n))
        print()
    # print(fib_bad(n))
