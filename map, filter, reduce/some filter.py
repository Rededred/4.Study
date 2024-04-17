
li = [1, 2, 3, 4, 5]
print([int(i) for i in filter(lambda x: False if x % 2 == 1 else True, li)])
print(list(filter(lambda x: x % 2 == 1, li)))

li2 = ['boo', 0, None, True, False, 1, 1-1, 2%2]
print(list(filter(None, li2)))

