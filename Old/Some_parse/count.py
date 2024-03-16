amount = 30000

capital = 0

rate = 1 + (0.1 / 12)
rate2 = 1 + (0.2 / 12)
rate3 = 1 + (0.3 / 12)


def per_year(a, c, r, r2, r3):
    for year in range(3):
        for month in range(12):
            c += a
            c *= r2
        a += 0.5*a
        print(year + 1, '~', c)


    for year in range(7):
        for month in range(12):
            c += a
            c *= r3
        a += 0.5*a
        print(year + 4, '~', c)


    # for year in range(2):
    #     for month in range(12):
    #         c += a
    #         c *= r
    #     print(year + 1, '~', c)
    #
    # a += 1000000
    # for year in range(2):
    #     for month in range(12):
    #         c += a
    #         c *= r2
    #     print(year + 3, '~', c)
    #
    # a += 1000000
    # for year in range(1):
    #     for month in range(12):
    #         c += a
    #         c *= r2
    #     print(year + 5, '~', c)
    #
    # # a += 1000000
    # for year in range(5):
    #     for month in range(12):
    #         c += a
    #         c *= r3
    #     print(year + 6, '~', c)

    #
    # for year in range(2):
    #     for month in range(12):
    #         c += a
    #         c *= r
    #     print(year + 1, '~', c)
    #     a += 200000

    # for year in range(3):
    #     for month in range(12):
    #         c += a
    #         c *= (1 + (0.3/12))
    #     print(year + 3, '~', c)
    #     a += 500000
    #
    # for year in range(2):
    #     for month in range(12):
    #         c += a
    #         c *= (1 + (0.3/12))
    #     print(year + 6, '~', c)
    #     a += 1000000


per_year(amount, capital, rate, rate2, rate3)
