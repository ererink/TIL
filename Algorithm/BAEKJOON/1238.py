# 파티

from heapq import heappop, heappush
import sys

INF = sys.maxsize

# 학생 수, 단방향 도로 개수, 파티장소(시작점)
n, m, p = map(int, input().split())
p -= 1

maps = [[] for _ in range(n)]
# 역방향 그래프 생성 => 돌아가는 시간 고려
rev_maps = [[] for _ in range(n)]

for _  in range(m):
    a, b, s = map(int, input().split())
    a -= 1
    b -= 1
    maps[a].append((s, b))
    rev_maps[b].append((s, a))

def party(p, board):
    heap = []
    heappush(heap, (0, p))      # 시작점(파티장소) 할당
    
    visited = [INF] * n
    visited[p] = 0
    
    while heap:
        cost, x = heappop(heap)
        
        if visited[x] < cost:
            continue
        
        for k, v in board[x]:
            min_cost = cost + k
            
            if visited[v] > min_cost:
                visited[v] = min_cost
                heappush(heap, (min_cost, v))

    return visited

# 함수실행 => 시작점이자 도착점인 노드와 길 정보가 있는 그래프 할당
visit = party(p, maps)              # 파티장소(p)에서 집으로 돌아가는 시간 측정
rev_visit = party(p, rev_maps)      # 집에서 파티장소로 가는 시간 측정

far = 0
for i in range(n):
    # 돌아갈때 걸리는 시간 + 갈때 걸리는 시간
    distance = visit[i] + rev_visit[i]
    
    # 걸리는 시간이 더 큰 수 찾아내기
    if far < distance:
        far = distance

print(far)