n, k, B, a = int(input()), 0, [], [0, 0]
while len(B) < n*2:
    B += input().lower().split()
for i in range(len(B)):
    if B[i] == 'север':
        a[1] += int(B[i+1])
    elif B[i] == 'юг':
        a[1] -= int(B[i+1])
    elif B[i] == 'восток':
        a[0] += int(B[i+1])
    elif B[i] == 'запад':
        a[0] -= int(B[i+1])
print(*a)