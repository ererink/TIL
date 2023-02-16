# 최소비용 구하기 2
from heapq import heappop, heappush
import sys

INF = sys.maxsize

n = int(input())
m = int(input())
maps = [[] for _ in range(n)]
visited = [INF] * n

for _ in range(m):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1
    maps[a].append((cost, b))

start, end = map(int, input().split())
start -= 1
end -= 1

heap = []
heappush(heap, (0, 1, [start + 1], start))   # 비용, 도시 개수, 경로, 위치
visited[start] = 0

while heap:
    cost, cnt, path, x = heappop(heap)
    
    if x == end:
        print(cost)
        print(cnt)
        print(*path)
        break
    
    if visited[x] < cost:
        continue
    
    for k, v in maps[x]:
        min_cost = cost + k
        
        if visited[v] > min_cost:
            visited[v] = min_cost
            heappush(heap, (min_cost, cnt + 1, path + [v + 1], v))