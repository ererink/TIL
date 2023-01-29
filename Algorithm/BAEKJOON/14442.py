# 벽 부수고 이동하기 2
from collections import deque

n, m, k = map(int, input().split())
maps = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * (k + 1) for _  in range(m)] for _ in range(n)]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    x, y, z =  queue.popleft()

    # (n, m)에 도달할 경우 정답 출력
    if x == n - 1 and y == m - 1:
        print(visited[x][y][z])
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            # 벽이지만 방문 하지 않았고 K보다 적게 벽 부수었을 경우 => 벽 부수기
            if maps[nx][ny] == 1 and z < k and visited[nx][ny][z + 1] == 0:
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                queue.append((nx, ny, z + 1))
            
            # 0인 길로 이동
            elif maps[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            

# (n, m)에 도달하지 못한다면 -1 출력
else:
    print(-1)

'''
특이사항
if maps[nx][ny] == 1 and z < k and visited[nx][ny][z + 1] == 0: 
    이 구문에서 
if maps[nx][ny] == 1 and visited[nx][ny][z + 1] == 0 and z < k : 
    일 경우 IndexError: list index out of range 에러 발생
'''