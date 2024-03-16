class Counter:
    def __init__(self, value):
        self.value = value

    # предопределение оператора сложения
    def __add__(self, other):

        # строго если обращаться к объектам!
        return Counter(self.value + other.value)

        # return Counter(self.value + other) #объект и число
        # return self.value + other
"""  
если как other передаётся не как 
объект класса Conter, а как число int 
(вместо "counter3 = counter1 + counter2"
было бы "counter3 = counter1 + 8")
"""


counter1 = Counter(7)
counter2 = Counter(8)

counter3 = counter1 + counter2
print(counter3.value)

# result = counter1 + 8
# print(result)
