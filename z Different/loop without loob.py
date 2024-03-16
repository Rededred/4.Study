def progression(start, stop, step):
    if start > stop:
        return
    else:
        print(start)
        progression(start+step, stop, step)

progression(0, 10, 1)
print('-'*15)
progression(0, 100, 5)