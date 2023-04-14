# 구슬 탈출 2

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

visited = [[[[False] * m for i in range(n)] for i in range(m)] for k in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            r1 = i; r2 = j
        elif board[i][j] == 'B':
            b1 = i; b2 = j


queue = deque()
queue.append((r1, r2, b1, b2, 0))
visited[r1][r2][b1][b2] = True

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    rx, ry, bx, by, cnt = queue.popleft()

    if cnt > 10:
        print(-1)
        break

    if board[rx][ry] == 'O':
        print(cnt)
        break

    for i in range(4):
        nrx = rx; nry = ry
        
        # RED 한 방향으로 계속 이동  
        while True:
            nrx += dx[i]
            nry += dy[i]

            if board[nrx][nry] == '#':    # 벽일 경우 한칸 뒤로
                nrx -= dx[i]
                nry -= dy[i]
                break

            if board[nrx][nry] == 'O':
                break

            
        
        # BLUE 한 방향으로 계속 이동 
        nbx = bx ; nby = by
        while True:
            nbx += dx[i]
            nby += dy[i]

            if board[nbx][nby] == '#':    # 벽일 경우 한칸 뒤로
                nbx -= dx[i]
                nby -= dy[i]
                break

            if board[nbx][nby] == 'O':
                break

            if nbx < 0 or nbx >= n or nby < 0 or nby >= m:
                break

        if board[nbx][nby] == 'O':  # 파란구슬이 들어갈 경우 무시
            continue

        if nrx == nbx and nry == nby:
            if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                nrx -= dx[i]; nry -= dy[i]
            else:
                nbx -= dx[i]; nby -= dy[i]
        
        if not visited[nrx][nry][nbx][nby]:
            visited[nrx][nry][nbx][nby] = True
            queue.append((nrx, nry, nbx, nby, cnt + 1))
else:
    print(-1)