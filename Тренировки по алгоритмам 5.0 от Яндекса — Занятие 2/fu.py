n = int(input())
N = sorted([int(i) for i in input().split()])
NN = list(reversed(N))
k = int(input())

def main(k, N, NN, n):
    rez = []
    for _ in range(k):
        a, b = [int(i) for i in input().split()]
        rez += [n - NN.index(b) - N.index(a)]
    return rez

print(*main(k, N, NN, n))
