import os.path

inf = open('3.44in.txt', 'r') # first way ���������
s1 = inf.readline() # ������ �����
s2 = inf.readline()
inf.close()

with open('text') as inf: # second way
    s1 = inf.readline()
    s2 = inf.readline()
    # ���� ����������� ���


s = inf.readline().strip() # ������� �� �������� ������, ������� ������

# import os
os.path.join('3.4 �������� ����', 'dirname', 'filename.txt') # ��������� ������� ���� � ����� (/��� ������� � ����, \��� �������)
'./dirname/filename.txt'

with open('input.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)

ouf = open('3.44in.txt', 'w') # first way ��������
ouf.write('�����-�� �������)\n')
ouf.write(str(25))
ouf.close()

with open('3.44out.txt', 'w') as ouf:
    ouf.write('�����-�� �����\n')
    ouf.write(str(25))