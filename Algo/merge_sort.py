from merge import Merge

def merge_sort(A):
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = Merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    return A

if __name__ == "__main__":
    rez = merge_sort(list(map(int, input().split())))
    print(rez)