# 행과 열의 순서가 바뀐 문제이다.

import sys
from collections import deque


input = sys.stdin.readline

dx = [0, 0, 1, -1, -1, 1, 1, -1] # 우 좌 하 상 우상 좌하 우하 좌상
dy = [1, -1, 0, 0, 1, -1, 1, -1]   # 0, 1 / -1, 1

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = True

    while queue:
        x, y = queue.popleft()                                      # 현재 (중심) 위치를 이동시켜준다. 

        for i in range(8):                                          # 8방이므로 range를 8로 설정한다. 
            nx = x + dx[i]                                          # 탐색 위치를 계속해서 바꿔준다. 
            ny = y + dy[i]  

            if 0 <= nx < m and 0 <= ny < n and not visit[nx][ny]:
                if maps[nx][ny] == 1:
                    visit[nx][ny] = True
                    queue.append((nx, ny))          #   queue:[(0,1)]

while True:
    n ,m = map(int, input().split())                                # n == 열, m == 행

    if n == 0 and m == 0:                                           # 문제 조건에 맞춰 0, 0이 나오면 입력 받는 것을 멈춘다. 
        break

    maps = [list(map(int, input().split())) for _ in range(m)]
    visit = [[False] * n for _ in range(m)]
    land = 0

    for i in range(m):                                              # n == 열, m == 행
        for j in range(n):      
            if maps[i][j] == 1 and not visit[i][j]:
                bfs(i, j)                                           # 값이 1이고 방문하지 않은 좌표를 새로운 현재 (중심) 위치를 이동시켜준다. 
                land += 1
    print(land)