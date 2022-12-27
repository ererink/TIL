# 적록색약
# 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.
'''
input = 5
        RRRBB
        GGBBB
        BBBRR
        BBRRR
        RRRRR

output = 4 3

1. 적록색약이 아닐때 영역의 개수를 구한다.
2. 적록색약일 때 R을 G로 바꿔준 후 영역 개수를 구한다. 
'''
from collections import deque

dx = [0, 0, 1, -1]	# 우 좌 하 상
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue.append((a, b))
    visit[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 인덱스 범위일 때, 같은 색일 때, 방문하지 않았을 때 이동한다.
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] == maps[x][y] and not visit[nx][ny]:
                    visit[nx][ny] = True
                    queue.append((nx, ny))


n = int(input())
maps = [list(input()) for _ in range(n)]
queue = deque()

# 적록색약이 아닌 경우
visit = [[False] * n for _ in range(n)]
color = 0                               # 영역
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            color += 1

# 적록색약인 경우
for i in range(n):
    for j in range(n):
        if maps[i][j] == 'R':           # R을 G로 바꿔주기
            maps[i][j] = 'G'
print(maps)

visit = [[False] * n for _ in range(n)]
no_color = 0
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            bfs(i, j)
            no_color += 1

print(color, no_color)
