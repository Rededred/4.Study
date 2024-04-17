def progression(start, stop, step):
    if start > stop:
        return
    else:
        print(start)
        progression(start+step, stop, step)
progression(0, 10, 1)

for i in range(10+1):
    print(i)
# print('-'*15)
# progression(0, 100, 5)


