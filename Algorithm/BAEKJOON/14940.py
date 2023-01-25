# 쉬운 최단거리
from collections import deque

# 세로, 가로
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
queue = deque()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        
        # 목표 지점을 찾은 후 목표지점부터 탐색 시작
        if maps[i][j] == 2:
            queue.append((i, j))
            
            while queue:
                x, y = queue.popleft()
                
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    
                    if 0 <= nx < n and 0 <= ny < m:
                        if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y] + 1
                            queue.append((nx, ny))


for k in range(n):
    for b in range(m):
        if maps[k][b] == 1:
            if visited[k][b] == 0:
                visited[k][b] = -1  # 도달하지 못한 좌표는 -1로 표시한다.
                
for i in visited:
    print(*i)
    
    