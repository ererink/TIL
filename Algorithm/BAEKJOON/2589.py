# 보물섬

from collections import deque

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]  

land = []
for k in range(n):
    for h in range(m):
        if maps[k][h] == 'L':
            now = deque()
            now.append((k, h))
            visit = [[0] * m for _ in range(n)]
            visit[k][h] = 1
            
            while now:
                x, y  = now.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                        if maps[nx][ny] == 'L':
                            visit[nx][ny] = visit[x][y] + 1
                            now.append((nx, ny))
            land.append(max(map(max, visit)))        

# 처음 시작을 1로 시작했기 때문
print(max(land) -1)
