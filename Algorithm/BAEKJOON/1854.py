# K번째 최단경로 찾기
from heapq import heappop, heappush
import sys
INF = sys.maxsize

n, m, K = map(int, input().split())
maps = [[] for _ in range(n)]
visited = [[INF] * K for _ in range(n)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    a -= 1 ; b -= 1
    maps[a].append((cost, b))

heap = []
heappush(heap, (0, 0))
visited[0][0] = 0

while heap:
    cost, x = heappop(heap)

    for k, v in maps[x]:
        min_cost = cost + k

        if visited[v][K - 1] > min_cost:
            visited[v][K - 1] = min_cost
            visited[v].sort()
            heappush(heap, (min_cost, v))

for i in range(n):
    if visited[i][K - 1] != INF:
        print(visited[i][K-1])
    else:
        print(-1)