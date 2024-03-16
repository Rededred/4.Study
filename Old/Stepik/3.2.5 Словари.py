def update_dictionary(d, key, value):
    # put your python code here
    if key in d:
        d[key] += [value]
    elif key * 2 in d:
        d[key * 2] += [value]
        return
    elif not (key * 2 in d):
        d[key * 2] = [value]
        return


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)