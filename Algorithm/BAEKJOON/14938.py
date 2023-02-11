# 서강그라운드
# 양방향 통행, 아이템의 최대 개수
from heapq import heappop, heappush
import sys

INF = sys.maxsize

# 지역개수, 수색범위, 길 개수
n, m, r = map(int, input().split())
items = list(map(int, input().split()))

maps = [[] for _ in range(n)]

for _ in range(r):
    a, b, s = map(int, input().split())
    a -= 1
    b -= 1
    # 양방향이므로 번갈아가면서 할당
    maps[a].append((s, b))
    maps[b].append((s, a))

max_ = 0

for d in range(n):
    heap = []
    heappush(heap, (0, d))

    visited = [INF] * n
    visited[d] = 0

    while heap:
        cost, x = heappop(heap)

        if visited[x] < cost:
            continue

        for k, v in maps[x]:
            min_cost = cost + k

            if visited[v] > min_cost:
                visited[v] = min_cost
                heappush(heap, (min_cost, v))

    cnt = 0
    for i in range(n):
        # 수색범위 확인
        if visited[i] <= m:
            cnt += items[i]

    if max_ < cnt:
        max_ = cnt

print(max_)
