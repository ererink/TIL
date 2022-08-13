# 1926
# 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라.
# 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 
# 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 

'''
input =
    6 5
    1 1 0 1 1
    0 1 1 0 0
    0 0 0 0 0
    1 0 1 1 1
    0 0 1 1 1
    0 0 1 1 1

output = 
    4
    9
'''
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]	# 우 좌 하 상
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()                                                    # 중심이 되는 위치를 이동시켜 주는 역할이다. 
    queue.append((a, b))
    visit[a][b] = True
    cnt = 1                                                            # 그림의 넓이, 1의 개수를 저장하는 역할이다. 

    while queue:
        x, y = queue.popleft()                                          # x, y는 4방 중 중심이 되는 현재 위치이다. 

        for i in range(4):
            nx = x + dx[i]                                              # nx, ny는 4방을 탐색하는 역할이다.
            ny = y + dy[i]                                              # 현재 위치에 델타 탐색 값을 더해서 탐색하는 좌표를 nx, ny에 저장해준다. 

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:       # 범위를 벗어나지 않고, 방문하지 않은 곳을 탐색한다. 
                if maps[nx][ny] == 1:                                   # 탐색 좌표가 1일 경우 탐색한다. 
                    cnt += 1                                            # 조건에 성립이 된다면 1을 추가한다. 
                    visit[nx][ny] = True                                # 방문처리한다.
                    queue.append((nx, ny))                              # 조건에 성립되는 탐색 좌표를 queue에 넣어준다. 
                                                                        # 현재 (중심) 위치가 nx, ny로 이동해주기 위함이다. 
    return cnt   


n ,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

        
visit = [[False] * m for _ in range(n)]
land = 0
land_cnt = 0

answer = []                                                             # 한 덩어리가 끝나게 되면 다시 돌아온다. 
for i in range(n):                              
    for j in range(m):
        if maps[i][j] == 1 and not visit[i][j]:                         # 좌표 중 값이 1이고, 방문하지 않은 곳을 다시 탐색한다. 
            answer.append(bfs(i, j))                                    # 새로운 현재 (중심) 위치가 된다. 
            land += 1

if len(answer) == 0:
    print(land)
    print(0)

else:
    print(land)
    print(max(answer))
                    
