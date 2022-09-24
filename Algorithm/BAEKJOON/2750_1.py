# 버블 정렬.ver

n = int(input())
a = [0] * n

for _ in range(n):
    a[_] = int(input())

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

for k in range(n):
    print(a[k])