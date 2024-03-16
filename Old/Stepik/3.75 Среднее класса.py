d = {}
class_info = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

with open('3.75 in.txt') as in_f_obj:
    for line in in_f_obj:
        string = line.rstrip().split('\t')
        if string[0] not in d:
            d[string[0]] = [int(string[2]), 1]
        elif string[0] in d:
            heights = d[string[0]][0] + int(string[2])
            students = d[string[0]][1] + 1
            d[string[0]] = [heights, students]

for k, v in d.items():
    class_info[int(k) - 1] = v[0] / v[1]


with open('3.75 out.txt', 'w+') as out_f_obj:
    for i in range(len(class_info)):
        output = str(i + 1) + ' ' + str(class_info[i]) + '\n'
        out_f_obj.write(output)
