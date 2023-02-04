# 최단경로

from heapq import heappop, heappush
import sys

INF = sys.maxsize

n, m = map(int, input().split())
start = int(input())
start -= 1

maps = [[] for _ in range(n)]
visited = [INF] * n
visited[start] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1
    
    maps[a].append((cost, b))

heap = []
heappush(heap, (0, start))

while heap:
    cost, x = heappop(heap)
    
    # 이미 적은 비용으로 지나간 최솟값이 있다면 밑 구문을 실행할 수 없다
    if visited[x] < cost:
        continue
    
    for k, v in maps[x]:
        min_cost = cost + k
        
        if visited[v] > min_cost:
            visited[v] = min_cost
            heappush(heap, (min_cost, v))

for i in visited:
    if i == INF:
        print('INF')
    else:
        print(i)