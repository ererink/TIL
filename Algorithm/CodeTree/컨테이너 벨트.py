# 시뮬레이션
from collections import deque

n, t = map(int, input().split())
queue = deque([])
for i in range(2):
    temp = list(map(int, input().split()))
    for j in range(n):
        queue.append(temp[j])

for i in range(t):
    temp = queue.pop()
    queue.appendleft(temp)

idx = 0
for i in range(n*2):
    print(queue[idx], end=" ")
    idx += 1
    if idx == n:
        print()