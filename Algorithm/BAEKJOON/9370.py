# 미확인 도착지
from heapq import heappop, heappush
import sys

INF = sys.maxsize

t = int(input())

for _ in range(t):
    # 교차로, 도로, 목적지 후보 개수
    n, m, t = map(int, input().split())
    # 출발지, 지나간 도로
    s, g, h = map(int, input().split())
    s -= 1
    g -= 1
    h -= 1
    maps = [[] for j in range(n)]
    for i in range(m):
        a, b, d = map(int, input().split())
        a -= 1
        b -= 1
    
        maps[a].append((d, b))
        maps[b].append((d, a))

    def measure(start):
        heap = []
        heappush(heap, (0, start))
        visited = [INF] * n
        visited[start] = 0

        while heap:
            cost, x = heappop(heap)

            if visited[x] < cost:
                continue
            for k, v in maps[x]:
                min_cost = cost + k
                if visited[v] > min_cost:
                    visited[v] = min_cost
                    heappush(heap, (min_cost, v))
        
        return visited
    
    case1 = measure(s)      # 입력값으로 주어진 출발지 (기본)   [0, 6, 8, 12, 11]
    case2 = measure(g)      # 지나간 도로                      [6, 0, 2, 6, 5]
    case3 = measure(h)      # 지나간 도로2                     [8, 2, 0, 4, 3]

    answer = []
    for i in range(t):
        goal = int(input())
        goal -= 1

        # 시작점, 특정한 도로 1  & 2, 목적지 후보의 길 측정
        path1 = case1[g] + case2[h] + case3[goal]
        path2 = case1[h] + case2[goal] + case3[g]

        if case1[goal] == path1 or case1[goal] == path2:
            answer.append(goal + 1)
        
    answer = sorted(answer)
    print(*answer)
