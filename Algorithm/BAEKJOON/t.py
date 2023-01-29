from collections import deque
import sys
N, M, K= map(int,input().split())
visited = [[[-1] * (K + 1) for _ in range(M)] for _ in range(N)]
matrix = [list(map(int,input().strip())) for _ in range(N)]
dx, dy = [0,0,1,-1],[1,-1,0,0]
visited[0][0][0] = 0
start = deque()
start.append((0,0,0))
while start:
    x, y, z = start.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y][z] + 1) # 시작하는 칸도 카운트를 해야하므로
        break
    for i in range(4):
        nx = x + dx[i]; ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if matrix[nx][ny] == 1 and z < K and visited[nx][ny][z + 1] == -1: # 다음 경로가 벽이고 현재 벽을 부순 z의 갯수가 총 부술 수 있는 갯수보다 작고, 이동 한 적이 없다면
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                start.append((nx, ny, z + 1))
            elif matrix[nx][ny] == 0 and visited[nx][ny][z] == -1: # 다음 경로가 길이고 이동한 적이 없다면,
                visited[nx][ny][z] = visited[x][y][z] + 1
                start.append((nx, ny, z))
else:
    print(-1) # break가 안걸린다면 실행