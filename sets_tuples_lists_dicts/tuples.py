andrey = ("Andrey", 21)
print(*andrey)

tuples_in_list = [('one', 'two'), ('three', 'four')]
print(*tuples_in_list)

print("----------------------")
tom = ("Tom", 37, "Google")
print(len(tom))
for parameter in tom:
    print(parameter)
print("----------------------")

def get_user():
    name = "Tommy"
    age = 22
    company = "Google"
    return name, age, company

user = get_user()
print(user)

