# 로봇

from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

s1, s2, s_dir = map(int, input().split())
s1 -= 1 ; s2 -= 1; s_dir -= 1
e1, e2, e_dir = map(int, input().split())
e1 -= 1 ; e2 -= 1; e_dir -= 1

queue = deque()
queue.append((s1, s2, s_dir))
visited[s1][s2][s_dir] = 0

# 동서남북 순서
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y, dirt = queue.popleft()

    if x == e1 and y == e2 and dirt == e_dir:
        print(visited[x][y][dirt])
        break
    
    # 3칸까지 직진 가능하기 때문에 범위 설정 1 ~ 4
    for i in range(1, 4):
        nx = x + (dx[dirt] * i)     # 현재 바라보는 방향으로 직진
        ny = y + (dy[dirt] * i) 
        
        if not (0 <= nx < n and 0 <= ny < m) or maps[nx][ny]:   # 범위를 벗어나거나 1을 만나면
            break

        if visited[nx][ny][dirt] == -1:
            visited[nx][ny][dirt] = visited[x][y][dirt] + 1
            queue.append((nx, ny, dirt))
    
    if dirt > 1:
        # 동, 서로 방향 바꾸기
        for i in range(2):
            if visited[x][y][i] == -1:
                visited[x][y][i] = visited[x][y][dirt] + 1
                queue.append((x, y, i))
        
    if dirt <= 1:
        # 남, 북으로 방향 바꾸기
        for i in range(2, 4):
            if visited[x][y][i] == -1:
                visited[x][y][i] = visited[x][y][dirt] + 1
                queue.append((x, y, i))               
