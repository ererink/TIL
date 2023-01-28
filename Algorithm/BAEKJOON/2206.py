# 벽 부수고 이동하기
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    x, y, z = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y][z])
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            # 벽이지만 방문한 적 없고 벽을 아직 부수지 않았을 때
            if maps[nx][ny] == 1 and visited[nx][ny][z] == 0 and z == 0:
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))
            
            # 길 이동
            elif maps[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            
            elif maps[nx][ny] == 0 and visited[nx][ny][z] == 0 and z == 1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

else:
    print(-1)