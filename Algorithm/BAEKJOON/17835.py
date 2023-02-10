# 면접보는 승범이네

from heapq import heappop, heappush
import sys

INF = sys.maxsize


n, m, k = map(int, input().split())

maps = [[] for _ in range(n)]

for _ in range(m):
    a, b, s = map(int, input().split())
    a -= 1
    b -= 1
    
    # 면접장이 시작점이 될 수 있도록 a - b가 아닌 b-a로 할당 (단방향)
    maps[b].append((s, a))

# 면접장 위치 k만큼 입력값 받기
place = list(map(int, input().split()))

visited = [INF] * n
heap = []

for i in place:
    i -= 1
    visited[i] = 0  # 면접장 위치가 시작점이기 때문에 0으로 할당
    heappush(heap, (0, i))

while heap:
    cost, x = heappop(heap)
    
    if visited[x] < cost:
        continue
    
    for k, v in maps[x]:
        min_cost = cost + k
        
        # min_cost가 더 최소비용이기 때문에 할당
        if visited[v] > min_cost:
            visited[v] = min_cost
            heappush(heap, (min_cost, v))

city = 0            # 가장 먼 도시 번호
distance = 0        # 가장 먼 도시와의 거리

# 도시의 수 만큼 반복하여 확인
for j in range(n):
    if visited[j] > distance:
        distance = visited[j]
        city = j + 1            # 위 구문에서 인덱스 번호때문에 1을 빼주었기 때문에

print(city)
print(distance)