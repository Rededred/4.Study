n, k, A= int(input()), 0, [] # ������ ���� ���������� ����
while k<n:
    a = input().lower()
    A += [a]
    k += 1

n, k, B = int(input()), 0, [] # ������ ���� ��� ��������
while k<n:
    b = input().lower().split()
    B += b
    k += 1

rez = []
for i in B: # �������� ���������
    if i not in A:
        if i not in rez:
            rez += [i]
        else:
            rez.remove(i)
            rez += [i]
    else:
        pass

for i in rez: # ������ ���������
    print(i, end='\n')

# ������ ������
# 4
# champions
# we
# are
# Stepik
# 3
# We are the champignons
# We Are The Champions
# Stepic