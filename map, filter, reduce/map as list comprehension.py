numbers = list(map(int, input().split()))
print(numbers)

numbers = list(map(bool, numbers))
print(numbers)

all_in_one = list(map(bool, list(map(int, input().split()))))
print(all_in_one)