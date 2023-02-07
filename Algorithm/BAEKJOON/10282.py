# 해킹 
from heapq import heappop, heappush
import sys

INF = sys.maxsize

t = int(input())
for _ in range(t):
    # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    n, d, c = map(int, input().split())
    c -= 1
    
    maps = [[] for _  in range(n)]
    visited = [INF] * n
    
    for i in range(d):
        a, b, s = map(int, input().split())
        a -= 1
        b -= 1

        # b -> a 로 감염(이동)
        maps[b].append((s, a))

    heap = []
    heappush(heap, (0, c))
    visited[c] = 0
    
    while heap:
        cost, x = heappop(heap)
        
        if visited[x] < cost:
            continue
        
        for k, v in maps[x]:
            min_cost = cost + k
            
            if visited[v] > min_cost:
                visited[v] = min_cost
                heappush(heap, (min_cost, v))
    
    # 감염된 컴퓨터 찾기
    cnt = 0     # 감염된 컴퓨터 수
    seconds = 0 # 걸린 시간
    for j in visited:
        if j != INF:    # INF가 아니라는 것은 이미 감염되었다는 것
            cnt += 1    # 감염된 컴퓨터의 수 + 1
            
            # 최대로 걸린 시간을 확인하며 할당해준다
            if seconds < j: 
                seconds = j
    
    print(cnt, seconds)
                