[print(i**2) if not i%15 else print(i) for i in range(1, 30+1)]
print('-'*15)
[print(i) for i in range(1, 40+1) if not i%8]

print('-'*15)
li_co_dict = {x: x*x for x in range(1, 30)}
print(li_co_dict)

print('-'*15)
[print(key,':', value) for key, value in {x: x*x for x in range(1, 30+1)}.items()]

print('-'*15)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
[print(i) for i in transposed_matrix]

print('-'*15)

