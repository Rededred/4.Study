a = str
b = []
dl = 0
while True:
    a = input()
    if a == str('end'):
        break
    b += [[int(i) for i in a.split()]]
    dl += 1
    sh = len(a.split())
dl = int(dl)
for i in range(dl):
    for j in range(sh):
        print(b[(i-1)][j] + b[(i+1)%dl][j] + b[i][j-1] + b[i][(j+1)%sh], end='  ')
    print()