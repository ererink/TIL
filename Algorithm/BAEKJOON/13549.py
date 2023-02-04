# 숨바꼭질 3
from heapq import heappop, heappush
import sys

INF = sys.maxsize
MAX = 100001

n, m = map(int, input().split())

maps = [[] for _ in range(n)]
visited = [INF] * (MAX)
visited[n] = 0

heap = []
heappush(heap, (0, n))

while heap:
    cost, x = heappop(heap)
    
    
    if x == m:
        print(cost)
        break
    
    for j in (x - 1, x + 1, x * 2):
        if 0 <= j < MAX and visited[j] == INF:
            # 최단경로를 찾기 때문에 * 2는 경로 측정에 포함하지 않는다.
            if j == x * 2:
                min_cost = cost
                
            # *2 이외 방법으로 이동할 경우 이동 시간을 1씩 더해준다.
            else:
                min_cost = cost + 1
        
            if visited[j] > min_cost:
                visited[j] = min_cost
                heappush(heap, (min_cost, j))