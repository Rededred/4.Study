from copy import deepcopy


def some_function(*, lst: list[int]) -> list[int]:
    lst.clear()
    return lst

my_list = [1, 2, 3, 4, 5]
new_list = some_function(lst=deepcopy(my_list))
print(my_list)
print(new_list)
