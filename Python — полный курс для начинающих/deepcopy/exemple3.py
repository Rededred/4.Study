def append_in_list(*, element: int, lst: list = []) -> list:
    lst.append(element)
    return lst
my_list = append_in_list(element=1)
print(my_list)
another_list = append_in_list(element=2)
print(my_list)
print(another_list)

print('---'*15)
def append_in_list2(*, element: int, lst: list = None) -> list:
    if lst is None:
        lst = []
    lst.append(element)
    return lst
my_list = append_in_list2(element=1)
print(my_list)
print()
another_list = append_in_list2(element=2)
print(my_list)
print(another_list)
