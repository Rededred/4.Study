import json

book = {
    'title': '1984',
    'author': 'George Orwell',
    'isbn': '978-045`5224935',
    'uuid': 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11',
    'count': 30,
    'genres': ['dystopia']

}
json_string = json.dumps(book)
print('Это Json строка:')
print(type(json_string))
print(json_string)

print()

print('Это не Json строка, а словарь:')
book = json.loads(json_string)
print(type(book))
print(book)