from functools import reduce

li = [2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(lambda x,y: x+y, li))

def try1(el_prev, el):
    print('     ', el_prev+el)
    return el_prev + el
def try2(el_prev, el):
    print('     ', el_prev)
    return el_prev + el
def try3(el_prev, el):
    # print('     ', el_prev)
    return el_prev**el

print(reduce(try1, li))
print(reduce(try2, li))
print(reduce(try3, li))
