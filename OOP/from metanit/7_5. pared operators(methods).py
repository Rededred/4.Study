class Counter:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other): return self.value == other.value
    def __ne__(self, other): return not (self == other)

    def __gt__(self, other): return self.value > other.value
    def __le__(self, other): return not (self > other)

    def __lt__(self, other): return self.value < other.value
    def __ge__(self, other): return not (self < other)

c1 = Counter(1)
c2 = Counter(2)

print(c1 == c2)
print(c1 != c2)

print(c1 < c2)
print(c1 >= c2)
