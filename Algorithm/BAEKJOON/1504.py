# 특정한 최단 경로

from heapq import heappop, heappush
import sys

INF = sys.maxsize

# 정점, 간선
n, m = map(int, input().split())

maps = [[] for _ in range(n)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1
    maps[a].append((cost, b))
    maps[b].append((cost, a))

v1, v2 = map(int, input().split())
v1 -= 1
v2 -= 1

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
            # measure 함수에 () 안에 있는 시작 지점 할당, 함수 실행 후 []에 위치한 값 비교 
            # 방문리스트에 기록된 소요 시간 중 제일 작은 값 출력
            # 0 -> v1 -> v2 -> n(끝) / 0 -> v2 -> v1 -> n => 두 가지 루트 비교
visit = min(measure(0)[v1] + measure(v1)[v2] + measure(v2)[n-1], measure(0)[v2] + measure(v2)[v1] + measure(v1)[n-1])

# visit 값이 INF면 방문하지 않았기 때문에
if visit < INF:
    print(visit)

else:
    print(-1)
