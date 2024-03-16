a = [int(i) for i in input().split()]
# a = input().split()
A = tuple(a)
b = len(a)
# n=0
if b == 1:
    print(a[0])
else:
    # while True:
    #     a[n] = int(A[n+1]) + int(A[n-1])
    #     n+=1
    #     if n+1 == b:
    #         a[n] = int(A[0]) + int(A[n - 1])
    #         break
    # for i in a:
    #     print(i, end=' ')

    for i in range(b):
        print(a[i-1] + a[(i+1)%b], end=' ')
