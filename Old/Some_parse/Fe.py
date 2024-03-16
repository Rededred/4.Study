n = int(input())

yeno = 0
s = 0
k = 0
while k < n:
    np = int(input())
    if np == 10:
        yeno += 1
    if np >= 5:
        s += 1
    k += 1

if yeno > 0:
    print("YES")
else:
    print("NO")

print(s)

n = int(input())
su = 0
yeno = 0
k = 0
while k in range(n):
    # np = int(input())
    # if np == 10:
    #     yeno += 1

    # if np >= 5:
    #     su+=1

    k += 1

