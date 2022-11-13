'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 

4 6
101111
101010
101011
111011
'''
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().rstrip())) for _ in range(n)]


dx = [0, 0, 1, -1] # 우 좌 하 상     
dy = [1, -1, 0, 0]

def bfs(x, y):                     
    queue = deque()                 
    queue.append((x, y)) 

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1

    return maps[n-1][m-1]

print(bfs(0,0))
