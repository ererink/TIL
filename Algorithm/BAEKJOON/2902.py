# KMP는 왜 KMP일까?

name = input()
temp = []

for i in name.split('-'):
    temp.append(i[0])

print(''.join(temp))

