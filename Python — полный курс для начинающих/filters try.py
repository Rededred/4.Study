def is_even(n: int) -> bool:
    return not n%2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(is_even, numbers)))

print(list(filter(lambda x: not x%2, numbers)))

print('-'*15)
people = [
    {'name': 'Alice', 'age': 17},
    {'name': 'Bob', 'age': 30},
    {'name': 'Diana', 'age': 19},
    {'name': 'Charlie', 'age': 40}
]
def is_adult(person:dict) -> bool:
    return person['age'] >= 18
print(list(filter(is_adult, people)))

print(list(filter(lambda people: people['age'] >= 18, people)))

print('-'*15)

