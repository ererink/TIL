# 사실 이 문제는 점프를 하며 주변을 쓰러트리는 식으로 구현해야 하나 라는 함정이 있지만, 잘 생각해보면
# 제자리에서 뛰었을때 4방향에 있는 사람들은 점프 1회를 소요한다는 것을 알 수 있음. 그래서 1이나 범인을 만나면 점프 + 1회 아니면 기존 값으로 사용하여 문제를 해결 할 수 있음
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
visited = [[INF] * M for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(N)]
start = []
sx -= 1; sy -= 1; ex -=1; ey -=1 # 맵의 위치와 sx,sy를 보면 인덱스 보다 +1 인걸 알 수 있음.
heappush(start, (0, sx, sy))
dx, dy = [0,0,1,-1], [1,-1,0,0]
visited[sx][sy] = 0
while start:
    jump, x, y = heappop(start)
    if jump > visited[x][y]:
        continue
    if x == ex and y == ey:
        print(jump)
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == '0': # 조건이 범인을 쓰러트리려면 이다보니 if == '1' 을 쓰게되면 조건문을 3가지 달아야하지만, 0이 아니면 쓰러트리라는 식으로 짧게 쓸 수 있음.
                next_jump = jump
            else:
                next_jump = jump + 1
            if visited[nx][ny] > next_jump:
                visited[nx][ny] = next_jump
                heappush(start, (next_jump, nx, ny))