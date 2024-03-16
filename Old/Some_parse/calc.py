def main():
    n = int(input("Процент:"))
    S = int(input("Ежемесячная сумма:"))
    m = int(input("Сколько месяцев:"))
    result = 100
    i = 0

    for i in range(m):
        result += S
        result *= (1 + (n / 100))

        i += 1

    print(result)


if __name__ == "__main__":
    while True:
        main()
        print("----------------------------------")

# https://www.desmos.com/calculator/6v30ciusxz