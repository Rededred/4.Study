class Counter:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value >= 0

def test(counter):
    if counter: print("Положительное или ноль")
    else: print("Отрицательное")


counter1 = Counter(3)
# test(counter1)
#
# counter2 = Counter(counter1.value - 6)
# test(counter2)


while counter1:
    print("Counter1: ", counter1.value)
    counter1.value -= 1
