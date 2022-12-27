'''
BFS

input = 4 6
        101111
        101010
        101011
        111011

output = 15
'''

from collections import deque

dx = [0, 0, 1, -1]	# 우 좌 하 상
dy = [1, -1, 0, 0]

n ,m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if maps[nx][ny] == 1:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1   # 이동

    return maps[n-1][m-1]

bfs(0,0)
print(maps[n-1][m-1])   # (n, m) 좌표까지 도달하도록 

