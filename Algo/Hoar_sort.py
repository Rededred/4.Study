def hoar_sort(A):
    if len(A) <= 1: return
    barrier = A[0]
    L, M, R = [], [], []
    for i in A:
        if i < barrier: L.append(i)
        elif i == barrier: M.append(i)
        else: R.append(i)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for i in L+M+R:
        A[k] = i
        k += 1
    return A

if __name__ == "__main__":
    print(hoar_sort([int(i) for i in input().split()]))
    print(hoar_sort(list(map(int, input().split()))))