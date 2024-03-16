"""массив должен быть отсортирован перед бинарным поиском"""

def left_bound(A, key):
    left = -1
    right = len(A)
    while right-left > 1:
        middle = (left + right)//2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return right

def right_bound(A, key):
    left = -1
    right = len(A)
    while right-left > 1:
        middle = (left + right)//2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

if __name__ == "__main__":
    test = [1, 3, 3, 6, 7, 9]
    print(left_bound(test, 5))
    print(right_bound(test, 5))