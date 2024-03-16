import random

print(random.random())
print(random.random() * 100)

print(random.randint(1, 100))

print(random.randrange(15))
print(random.randrange(15, 17))  # 17 не включительно
print(random.randrange(15, 35, 5))  # 35 не включительно

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(numbers)
random_number = random.choice(numbers)
print(random_number)