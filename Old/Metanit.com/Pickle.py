import pickle

FILENAME = 'user.dat'

name = 'Andrey'
age = 20

with open(FILENAME, 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME, 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print('Имя:', name, '\tВозраст:', age)


users = [
    ['Tom', 28, True],
    ['Alice', 23, False],
    ['Bob', 34, False]
]

with open(FILENAME, 'wb') as file:
    pickle.dump(users, file)

with open(FILENAME, 'rb') as file:
    user_from_file = pickle.load(file)
    for user in user_from_file:
        print('Имя:', user[0], '\tВозраст:', user[1], '\tЖенат(замужем):', user[2])