# 지름길

from collections import deque

# 노드, 간선, 거리정보, 출발노드
n, m, k, s = map(int, input().split())
maps = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
queue = deque()
queue.append(s)
visited[s] = 0
path = []
flag = False
while queue:
    x = queue.popleft()
    if visited[x] == k:
        path.append(x)
        flag = True
    for i in maps[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            queue.append(i)
path.sort()
for i in path:
    print(i)
            
if flag == False:
    print(-1)