# 오목

from collections import deque
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]  # 우 하 우하 우상
dy = [1, 0, 1, 1]
visited = [[False] * 19 for _ in range(19)]

queue = deque()
check = 0
for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            check = board[x][y]     # 1 or 2

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                cnt = 1

                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == check:
                    cnt += 1

                    if cnt == 5:
                        if 0 <= x - dx[i]< 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == check:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == check:
                            break

                        print(check)
                        print(x + 1, y + 1)
                        # sys.exit(0)
                    
                    nx += dx[i]
                    ny += dy[i]
       
print(0)