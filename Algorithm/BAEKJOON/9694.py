# 무엇을 아느냐가 아니라 누구를 아느냐가 문제다

from heapq import heappop, heappush
import sys

INF = sys.maxsize

t = int(input())
cnt = 0

for _ in range(t):
    n, m = map(int, input().split())    # 관계 개수, 정치인 수
    maps = [[] for _ in range(m)]
    visited = [INF] * m
    
    for i in range(n):
        a, b, cost = map(int, input().split())  # 0은 한신, m-1은 최고의원
        maps[a].append((cost, b))
        maps[b].append((cost, a))
    
    heap = []
    heappush(heap, (0, [0], 0))     # cost, 경로, 출발지
    visited[0] = 0
    
    cnt += 1
    print(f'Case #{cnt}:', end = ' ')
    while heap:
        cost, path, x = heappop(heap)
        
        if x == m - 1:
            print(*path)
            break
        
        if visited[x] < cost:
            continue
        
        for k, v in maps[x]:
            min_cost = cost + k
            
            if visited[v] > min_cost:
                visited[v] = min_cost
                heappush(heap, (min_cost, path + [v], v))

    else:
        print(-1)
