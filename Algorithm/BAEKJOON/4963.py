# 섬의 개수
# BFS
# 8방향

'''
1 1 => 너비와 높이 
0
2 2 => 너비와 높이
0 1
1 0
3 2 => 너비와 높이
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1, -1, 1, 1, -1] # 우 좌 하 상 우상 좌하 우하 좌상
dy = [1, -1, 0, 0, 1, -1, 1, -1] 


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

while True:
    n, m = map(int, input().split())    # n == 가로 m == 세로

    if n == 0 and m == 0:               # 가로, 세로 길이가 0으로 주어질 경우
        break
    
    graph = [list(map(int, input().split())) for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    land = 0

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                land += 1
    print(land)
