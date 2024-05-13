import pickle
import json

class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def describe_fruit(self):
        print(self.name, self.calories, sep=': ')

if __name__ == '__main__':
    # можно обозначать экземляр класса таким образом, так как так явней
    # fruit: Fruit = Fruit('banana', 100)
    fruit = Fruit('Banana', 100)
    fruit.describe_fruit()

    fruit.calories = 150
    with open('banana.json', 'w') as file:
        data = {'name': fruit.name, 'calories': fruit.calories}
        json.dump(data, file)

    with open('banana.json', 'r') as file:
        data = json.load(file)
        print(data)
