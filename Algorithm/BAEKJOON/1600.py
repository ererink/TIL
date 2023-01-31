# 말이 되고픈 원숭이
from collections import deque

k = int(input())
# 세로 가로
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]
visited = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)
hx = [-2, -1, 1, 2, 2, 1, -1, -2]
hy = [-1, -2, -2, -1, 1, 2, 2, 1]


while queue:
    # z는 원숭이가 말처럼 움직일 수 있는 횟수를 저장한다.
    x, y, z = queue.popleft()

    if x == (m - 1) and y == (n - 1):
        print(visited[x][y][z])
        break

    # k번 까지 말의 움직임을 따라한다
    if z < k:
        
        for i in range(8):
            nhx = x + hx[i]
            nhy = y + hy[i]

            if 0 <= nhx < m and 0 <= nhy < n:
                if maps[nhx][nhy] == 0 and visited[nhx][nhy][z + 1] == -1:
                    # 말은 장애물을 뛰어넘을 수 있다.
                    visited[nhx][nhy][z + 1] = visited[x][y][z] + 1
                    queue.append((nhx, nhy, z + 1))
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if maps[nx][ny] == 0 and visited[nx][ny][z] == -1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

else:
    print(-1)