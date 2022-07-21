# 오답
n = int(input())
clap = ['3', '6', '9']

for i in range(1, n + 1):
    i = str(i)
    if i in clap:
        print('-', end = ' ')
    else:
        print(i, end = ' ')
        continue

# 모범 답안
n = int(input())
for i in range(1, n + 1):
    i = str(i)
    c = i.count('3') + i.count('6') + i.count('9')

    if c == 0:
        print(i, end=' ')
    else:
        print('-' * c, end=' ')