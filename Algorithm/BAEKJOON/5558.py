# チーズ (Cheese)

from collections import deque

n, m, k = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]


queue = deque()
# 시작지점 S 찾기
for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            queue.append((i, j, 0))
            break

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cheese = 1
while queue:
    x, y, z = queue.popleft()
    
    if z == k:
        print(visited[x][y][z])
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            # 치즈 찾기
            if maps[nx][ny] == str(cheese) and z + 1 == cheese and visited[nx][ny][z] == 0:
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                cheese += 1
                queue.append((nx, ny, z + 1))
            
            # 길 이동
            # 비교대상이 '.'이 아닌 'X'로 설정해야 하는 이유는 지나가는 길이 현재 찾지 않는 치즈번호일 수도 있기 때문에
            elif maps[nx][ny] != 'X' and maps[nx][ny] != str(cheese) and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
