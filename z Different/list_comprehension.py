dictionary = {"red": "красный", "blue": "синий", "green": "зеленый"}

di = [f'\n{n} = {p}' for n, p in dictionary.items()]
print(*di)  #пример раскрытия всего словаря в красивый столбик

numbers = [-3, -2, -1, 0, 1, 2, 3]
print(*[n**2 for n in numbers if -3 < n < 3])  #пример перебора просто чисел
print(*[n**2 for n in numbers if n**2 != 4])

# newlist = [expression for item in iterable( if condition)]