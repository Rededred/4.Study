n, k, B, a = int(input()), 0, [], [0, 0]
while len(B) < n*2:
    B += input().lower().split()
for i in range(len(B)):
    if B[i] == '�����':
        a[1] += int(B[i+1])
    elif B[i] == '��':
        a[1] -= int(B[i+1])
    elif B[i] == '������':
        a[0] += int(B[i+1])
    elif B[i] == '�����':
        a[0] -= int(B[i+1])
print(*a)