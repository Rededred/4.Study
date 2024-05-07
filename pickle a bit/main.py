import pickle
import json

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def describe_friut(self):
        print(self.name, self.calories, sep=': ')

if __name__ == '__main__':
    # можно обозначать экземляр класса таким образом, так как так явней
    # friut: Fruit = Fruit('banana', 100)
    fruit = Fruit('banana', 100)
    fruit.describe_friut()