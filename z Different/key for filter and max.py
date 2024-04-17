fruits = ['banana', 'apple', 'cherry', 'data']

print(sorted(fruits, key=lambda el: len(el)))
print(list(reversed(sorted(fruits, key=lambda el: len(el)))))
print(max(fruits, key=lambda el: len(el)))