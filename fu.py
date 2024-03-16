"""
кузнечик прыгает до точки N прыжками длиной 1 или 2
--1--2--3--4--5--6-- ... --N-2--N-1--N
найти количество возможных комбинаций прыжков (ответ в нахождении числа фибоначи)

"""
def traj_num(n):
    K = [0,1]+[0]*n
    for i in range(2, n+1):
        K[i] = K[i-2]+K[i-1]
    return K[n]
print(traj_num(15))

"""
как решать, если есть запрещённые клетки?
"""
def count_trajectories(N, allowed:list):
    k = [0, 1, int(allowed[2])] + [0]*(N-3)
    for i in range(3, N+1):
        if allowed[i]:
            k[i] = k[i-1]+k[i-2]+k[i-3]
    return k[N]
print(count_trajectories(15, [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]))
