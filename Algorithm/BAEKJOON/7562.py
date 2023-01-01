'''
나이트의 이동

나이트는 몇 번 움직이면 나이트가 이동하려고 하는 칸으로 이동할 수 있을까?

input = 3
        8
        0 0
        7 0
        100
        0 0
        30 50
        10
        1 1
        1 1

output = 5
        28
        0
'''

from collections import deque


dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs():
    queue = deque()
    queue.append((now_r, now_c))

    while queue:
        x, y = queue.popleft()
        if x == arr_r and y == arr_c:
            return maps[x][y] - 1       # 도착했다면 현재 위치에서 -1을 빼준다 (출발지가 이미 1이기 때문에)

        for i in range(8):
            nx = x + dx[i]  
            ny = y + dy[i] 

            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))  


testcase = int(input())
answer = []
for _ in range(testcase):
    n = int(input())    # 체스판 한 변의 길이
    now_r, now_c = map(int, input().split())    # 현재 위치
    arr_r, arr_c = map(int, input().split())    # 도착 위치
    maps = [[0] * n for _ in range(n)]          # 체스판
    maps[now_r][now_c] = 1
    print(bfs())
