# 주난의 난

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

INF = sys.maxsize

n, m = map(int, input().split())
visited = [[INF] * m for _ in range(n)]

# 주난의 위치, 범인의 위치
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1

maps = [list(input().rstrip()) for _ in range(n)]

heap = []
# 주난의 위치 할당 => 출발지
heappush(heap, (0, x1, y1))
visited[x1][y1] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    cost, x, y = heappop(heap)
    
    # 최소비용이 아니므로 실행할 수 없음
    if visited[x][y] < cost:
        continue
    
    if x == x2 and y == y2:
        print(cost)
        break
    
    for i in  range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            # 친구 및 범인을 탐색하는 경우가 '0이 아닐 때' 이므로 '0을 탐색할 때'의 조건문 1개만 써준다.
            if maps[nx][ny] == '0':
                min_cost = cost
            
            # 친구 혹은 범인을 탐색할 경우
            else:
                min_cost = cost + 1
            
            if visited[nx][ny] > min_cost:
                visited[nx][ny] = min_cost
                heappush(heap, (min_cost, nx, ny))