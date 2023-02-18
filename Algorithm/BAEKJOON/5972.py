# 택배 배송

from heapq import heappop, heappush
import sys

INF = sys.maxsize

n, m = map(int, input().split())
maps = [[] for _ in range(n)]
visited = [INF] * n

for _ in range(m):
    a, b, cost = map(int, input().split())
    a -= 1; b -= 1
    maps[a].append((cost, b))
    maps[b].append((cost, a))

heap = []
heappush(heap, (0, 0))
visited[0] = 0

while heap:
    cost, x = heappop(heap)

    if visited[x] < cost:
        continue

    for k, v in maps[x]:
        min_cost = cost + k

        if visited[v] > min_cost:
            visited[v] = min_cost
            heappush(heap, (min_cost, v))
            
print(visited[n-1])