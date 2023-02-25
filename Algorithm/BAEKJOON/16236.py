# 아기상어
from collections import deque
import sys
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
INF = sys.maxsize
for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            a = i ; b = j
            maps[i][j] = 0
            break

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


shark = 2
move_n = 0
eat = 0
while True:
    queue = deque()
    queue.append((a, b, 0))
    visited = [[False] * n for _ in range(n)]
    flag = INF
    fish = []
    while queue:
        x, y, cnt = queue.popleft()

        if cnt > flag:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if maps[nx][ny] > shark or visited[nx][ny] == True:
                continue

            if maps[nx][ny] != 0 and maps[nx][ny] < shark:
                fish.append((nx, ny, cnt + 1))
                flag = cnt
            visited[nx][ny] = True
            queue.append((nx, ny, cnt + 1))

    if len(fish) > 0:
        fish.sort()
        x, y, move = fish[0][0], fish[0][1], fish[0][2]
        move_n += move
        eat += 1
        maps[x][y] = 0
        if eat == shark:
            shark += 1
            eat = 0
        a = x; b = y
    else:
        break
print(move_n)
