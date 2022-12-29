'''
토마토

보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.

input = 6 4
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 1

output = 8
'''
from collections import deque


m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 1 and not visit[i][j]:     # 시작할 익은 토마토 찾기
            queue.append([i,j])

dx = [0, 0, 1, -1]	# 우 좌 하 상
dy = [1, -1, 0, 0]

def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if maps[nx][ny] == 0:
                    visit[nx][ny] = True
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1    # 하나씩 더해서 제일 큰값 찾기
          
bfs()
answer = 0
for i in maps:
    for j in i:
        if j == 0:
            print(-1) # 익은 토마토가 있으면 -1 출력
            exit(0)
    answer = max(answer, max(i))    # max 매개변수 중 제일 큰 값 출력

print(answer - 1)   # 처음에 1인 상태에서 + 1을 해주었으니 -1 해준다.

    
    