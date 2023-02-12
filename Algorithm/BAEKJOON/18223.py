# 민준이와 마산 그리고 건우
from heapq import heappop, heappush
import sys

INF = sys.maxsize

# 정점, 간선, 건우 위치
n, m, p = map(int, input().split())
p -= 1

maps = [[] for _  in range(n)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1

    # 양방향
    maps[a].append((cost, b))
    maps[b].append((cost, a))

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

n1 = measure(0)     # 시작 노드 값을 0으로 넣은 방문 리스트 출력 [0, 1, 1, 2, 3, 4] => 시작노드부터 마산까지의 일반적인 최단거리 구함
n2 = measure(p)     # 건우가 위치한 노드가 시작값 [2, 3, 1, 0, 1, 2]

# 마산에 도착한 최단거리가 건우 위치와 건우 위치를 시작으로 마산까지 도착하는 거리와 같으면 이는 최단거리임을 뜻한다.
if n1[n-1] == n1[p] + n2[n-1]:
    print('SAVE HIM')
else:
    print('GOOD BYE')