users = {"Tom", "Bob", "Alice", "Madi"}

print('----------------------------')
for user in users: print(user)

users.remove('Tom')
# users.remove("sadf")  #нельзя, так как нет в сете
users.discard('Bob')
users.discard('Alice')
users.discard('sadf')  #можно, метод позволяет

print('----------------------------')
my_love = users.copy()
users.clear()
print(my_love)

me = {"Andrey"}
we = me.union(my_love)
print(we)
print(me | my_love)

print('----------------------------')
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.intersection(users2)  #пересечение множеств
print(users3)
print(users.intersection(users2))
print(users & users2)
users.intersection_update(users2)  #заменяет пересечением первое множество
print(users)

print('----------------------------')
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.difference(users2)  #обычная разность
print(users3)
print(users - users2)

print('----------------------------')
users3 = users.symmetric_difference(users2)  #симметричная разность
print(users3)
print(users.symmetric_difference(users2))
print(users ^ users2)

print('----------------------------')
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}

print(users.issubset(superusers))  #является ли субсетом
print(superusers.issubset(users))
print()
print(users.issuperset(superusers))  #является ли суперсетом
print(superusers.issuperset(users))

print('----------------------------')
users = frozenset({"Tom", "Bob", "Alice"})
u = set(users.copy())  #переопределять только так
u.add("asdf")
print(u)

