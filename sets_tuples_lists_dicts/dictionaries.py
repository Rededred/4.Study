users = {1: "Tom", 2: "Bob", 3: "Bill"}

print('-------------------------')
for key in users.keys():
    print(key, users[key])

print('-------------------------')
users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
dicto = dict(users_list)
del dicto["+384767557"]
print(dicto.pop("+111123455"))  # просто удаляет ключ-значение
print(dicto.pop("+111123455", "\'выведется, если нет такого ключа\'"))
print(dicto)

print('-------------------------')
users = {"+1111111": "Tom", "+3333333": "Bob"}
users2 = {"+2222222": "Sam", "+6666666": "Kate"}
x = users.copy()
x.update(users2)
print(x)

print('-------------------------')
users = {1: "Tom", 2: "Bob", 3: "Bill"}
for key, value in users.items(): print(key, value)
for key, value in users.items(): print(f"Ключ:{key}   Значение: {value}")

print('-------------------------')
users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}
print(*users)
print(users.keys())
print(*users.values())

old_email = users["Tom"]["email"]
users["Tom"]["email"] = "sfasdf@ya.ru"
print(users['Tom'])
tom_skype = users["Tom"].get('Skype', 'Undefined')
print(tom_skype)