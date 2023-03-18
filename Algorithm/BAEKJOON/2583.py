from collections import deque

N, M, K = map(int, input().split())
board = [[0] * M for _  in range(N)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def count(x, y):
    cnt = 0
    board[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                cnt += 1
                queue.append((nx, ny))
    return cnt

answer = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
           answer.append(count(i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i + 1, end=" ")