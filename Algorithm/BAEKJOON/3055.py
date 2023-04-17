from collections import deque
n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)] 

flood = deque()
queue = deque()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            queue.append((i, j, 0))
            visited[i][j] = True
        
        elif maps[i][j] == '*':
            flood.append((i, j))


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    # 홍수 진행
    for _ in range(len(flood)):
        wx, wy = flood.popleft()

        for i in range(4):
            nfx = wx + dx[i]
            nfy = wy + dy[i]

            if 0 <= nfx < n and 0 <= nfy < m and maps[nfx][nfy] == '.':
                maps[nfx][nfy] = '*'        # 물이 차오른 곳을 '*'로 바꾸어 고슴도치가 이동하지 못하게 한다.
                flood.append((nfx, nfy))

    # 고슴도치 이동
    for _ in range(len(queue)):
        x, y, cnt = queue.popleft()

        if maps[x][y] == 'D':
            print(cnt)
            exit()                      # for문과 while문 종료

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]


            if  0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] != '*' and maps[nx][ny] != 'X':     # 'D'를 인식해야 하므로 "== '.'" 로 탐색하지 않는다.
                    visited[nx][ny]= True
                    queue.append((nx, ny, cnt + 1))

else:
    print("KAKTUS")