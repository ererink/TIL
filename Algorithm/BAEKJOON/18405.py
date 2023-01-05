# 경쟁적 전염

from collections import deque

# 시험관 크키, 바이러스 종류 개수
n, k = map(int, input().split())   
maps = [list(map(int, input().split())) for _ in range(n)]

# 시간, 좌표 위치
s, x, y = map(int, input().split())

# maps 인덱스는 0부터 시작하기 때문
x = x -1
y = y - 1

now = []
for i in range(n):
    for j in range(n):
        if maps[i][j] != 0:
                    # 바이러스 번호, 바이러스 위치, 시간
            now.append((maps[i][j], i , j , 0)) # 튜플 형식으로 할당

now = deque(sorted(now))  # 바이러스 번호 정렬
                          # 1, 2, 3 순서로 바이러스가 확장해야 하기 때문에
# 우 좌 하 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while now:
    num, a, b, sec = now.popleft()

    if sec == s:    # 조건 시간이 되면 멈춘다
        break

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 0:
                maps[nx][ny] = num 
                now.append((num, nx, ny, sec + 1))

print(maps[x][y])