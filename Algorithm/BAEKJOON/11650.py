# 람다 함수

'''
5
3 4
1 1
1 -1
2 2
3 3
'''

n = int(input())
a = []

for _ in range(n):
    b, c = (map(int, input().split()))
    a.append((b, c))

a.sort(key=lambda x: (x[0], x[1]))

for i in a:

    print(*i)