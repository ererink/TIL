# 최소비용 구하기

from heapq import heappop, heappush
import sys

INF = sys.maxsize

n = int(input())
m = int(input())
maps = [[] for _ in range(n)]
visited = [INF] * n

# 정점과 간선의 정보 받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1
    
    maps[a].append((cost, b))

start, end = map(int, input().split())
start -= 1
end -= 1
visited[start] = 0

heap = []
heappush(heap, (0, start))

while heap:
    cost, x = heappop(heap)
    
    # 최소비용으로 지나간 흔적이 있다면 현재 cost를 기준으로 탐색X
    if visited[x] < cost:
        continue
    
    for k, v in maps[x]:
        min_cost = cost + k
        
        if visited[v] > min_cost:
            visited[v] = min_cost
            heappush(heap, (min_cost, v))

print(visited[end])