# 로봇

from collections import deque

n, m = map(int, input().split())
# 청소기 현재위치, 방향
r, c, d =map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 0 3 2 1 순서, 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 현재 위치 방문 처리
visited[r][c] = True
cnt = 1

while True:
    flag = 0    # 4방향 탐색 완료 변수
    # 4방향 탐색
    for i in range(4):
        nx = r + dx[(d + 3) % 4]
        ny = c + dy[(d + 3) % 4]
        d = (d + 3) % 4
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if maps[nx][ny] == 0:
                visited[nx][ny] = True
                cnt += 1
                # 이동
                r = nx
                c = ny
                flag = 1
                break
    
    # 4방향을 모두 청소했을 때         
    if flag == 0:     
        if maps[r - dx[d]][c - dy[d]] == 1:
            print(cnt)
            break
        
        else:
            r, c = r - dx[d], c - dy[d]
        