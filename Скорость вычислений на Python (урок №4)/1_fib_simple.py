import time

final_fibonacci_number = 40

def fib(n: int) -> int:
    return fib(n-1) + fib(n-2) if n > 2 else 1

def main():
    tasks = list(range(0, final_fibonacci_number + 1))
    start_time = time.perf_counter()
    # без параллельных вычислений
    answers = []
    for number in tasks:
        answers.append(fib(number))
    # Работает один родительский процесс
    finish_time = time.perf_counter()
    print('Duration', finish_time - start_time)
    print(*answers)

if __name__ == '__main__':
    main()