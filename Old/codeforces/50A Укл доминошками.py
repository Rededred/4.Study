
size = input().split()
a = int(size[0])
b = int(size[1])

if a % 2 == 0:
    print(int((a/2)*b))
else:
    print(int(((a-1)/2)*b+(b//2)))
