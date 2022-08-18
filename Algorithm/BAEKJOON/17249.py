# 태보태보 총난타

location = 0
p = [0, 0]

for i in input():
    if i == '@':
        p[location] += 1

    elif i == '(':
        location += 1

print(*p)
    