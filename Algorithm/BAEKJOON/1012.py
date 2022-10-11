# 유기농 배추
# BFS
'''
2           => 케이스의 개수
10 8 17     => 배추밭의 가로길이, 세로길이, 배추 위치의 개수
0 0         => 배추의 위치
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''
import sys
from collections import deque

input = sys.stdin.readline


dx = [0, 0, 1, -1] # 우 좌 하 상     
dy = [1, -1, 0, 0]


def bfs(a, b):                     
    queue = deque()                 
    queue.append((a, b)) # 튜플       queue = [(0, 0)]   현재위치 
    visit[a][b] = True          

    while queue: # 큐가 빌 때 까지      
        x, y = queue.popleft()       # x, y = [(0, 0)]  현재위치
                                    # x == 0, y == 0
        for i in range(4):
            nx = x + dx[i]          # next x, next y 즉, 탐색을 해줄 방향 지시
                                    # (x) 0 + (dx)0 = 0
            ny = y + dy[i]          # (x) 0 + (dx)1 = 1

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if maps[nx][ny] == 1:
                    visit[nx][ny] = True
                    queue.append((nx, ny))

    return

t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]
    visit = [[False] * m for j in range(n)]
    cnt = 0

    for j in range(k):
        x, y = map(int, input().split())
        maps[x][y] = 1

    for k in range(n):
        for v in range(m):
            if maps[k][v] == 1 and not visit[k][v]:
                bfs(k, v)
                cnt += 1

    print(cnt)