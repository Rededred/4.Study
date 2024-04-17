fruits = ['banana', 'apple', 'cherry', 'date']

print(sorted(fruits))

fruits.sort()
print(fruits)

print('-'*15)
def sort_by_len(element):
    return len(element)
print(sort_by_len)
print(type(sort_by_len))
print(sorted(fruits, key=sort_by_len))
print(sorted(fruits, key=len))

print('-'*15)
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 20},
    {'name': 'Diana', 'age': 30},
    {'name': 'Charlie', 'age': 30}
]
def sort_by_age(person) -> int:
    return person['age']
print(sorted(people, key=sort_by_age))
print(sorted(people, key=lambda people: people['age']))

print('-'*15)
def sort_by_age_name(element: dict) -> tuple[int, str]:
    return element['age'], element['name']
print(sorted(people, key=sort_by_age_name))

print('-'*15)

