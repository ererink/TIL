# 공주님을 구해라!

from collections import deque

n, m, t = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append((0, 0, 0))


while queue:
    x, y, z = queue.popleft()
    
    if x == n - 1 and y == m - 1:
        if visited[x][y][z] <= t:
            print(visited[x][y][z])
            break
        
        else:
            print('Fail')
            break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:

            if visited[nx][ny][z] == 0 and z == 1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
                        

            elif maps[nx][ny] == 0 and visited[nx][ny][z] == 0 and z == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            
            # 그람 발견
            elif maps[nx][ny] == 2 and visited[nx][ny][z] == 0 and z == 0:
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))
        
else:
    print('Fail')
