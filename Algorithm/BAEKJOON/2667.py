'''
단지번호붙이기
연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

input = 7
        0110100
        0110101
        1110101
        0000111
        0100000
        0111110
        0111000

output = 3
        7
        8
        9
'''
from collections import deque

dx = [0, 0, 1, -1]	# 우 좌 하 상
dy = [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if maps[nx][ny] == 1:
                    cnt += 1
                    visit[nx][ny] = True
                    queue.append((nx, ny))
    return cnt

n = int(input())
maps = [list(map(int, input())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
land = 0
answer = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and not visit[i][j]:
            answer.append(bfs(i, j))
            land += 1
print(land)

answer = sorted(answer)
for num  in answer:
    print(num)