class Counter:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value


counter1 = Counter(1)
counter2 = Counter(2)

if counter1 > counter2: print("первый больше второго")
elif counter1 < counter2: print("первый меньше второго")
else: print("каунтеры равны")