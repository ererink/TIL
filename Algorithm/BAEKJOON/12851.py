# 숨바꼭질

'''
input = 5 17

output = 4
         2
'''
from sys import stdin
from collections import deque
input = stdin.readline

# 수빈 & 동생 위치
n, k = map(int, input().split())
MAX = 100001

dist = [-1] * (MAX)
dist[n] = 0

queue = deque()
queue.append(n)
cnt = 0

while queue:
    # 현재위치
    x = queue.popleft()

    # 동생 위치에 도착
    if x == k:
        cnt += 1
    
    # 이동
    for j in (x - 1, x + 1, x * 2):
        # 범위 내 일 때
        if 0 <= j < MAX:
            # 방문 시간이 같은 경우가 이미 있을 때 
            if dist[j] == -1 or dist[j] >= dist[x] + 1:
                dist[j] = dist[x] + 1
                queue.append(j)


print(dist[k])
print(cnt)