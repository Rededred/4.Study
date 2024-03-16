def check_sort(A, ascending=True):
    """Проверка отсотрированности за O(len(A))"""
    flag = True
    s = 2*int(ascending) - 1
    for i in range(0, len(A)-1):

        if s*A[i] > s*A[i+1]:
            flag = False
            break
    return flag

print(check_sort([0, 1, 2, 3, 4, 5, 8, 29]))
print(check_sort([0, 1, 2, 3, 4, 5, 8, 7, 29]))