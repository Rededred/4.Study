def dodo(f):
    floor = f//20+1 if f%20 else f//20
    print('Подъезд:', floor, "Этаж:", ((f-1)%20)//4+1, end=' ')

if __name__ == '__main__':
    flat_number = 100
    for i in range(1, flat_number+1):
        dodo(i), print(' Квартира: ', i)
        if not i%4:
            print('---------------')
    # while True:
        # flat_number = int(input())
        # dodo(flat_number)
