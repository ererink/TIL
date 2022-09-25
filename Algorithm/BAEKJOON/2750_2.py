# 삽입 정렬.ver

n = int(input())
a = [0] * n

for _ in range(n):
    a[_] = int(input())

for i in range(1, len(a)):
    while (i > 0) and (a[i] < a[i-1]):
        a[i], a[i - 1] = a[i-1], a[i]
    
        i -= 1

for j in a:
    print(j)