# 일요일 아침의 데이트

from heapq import heappop, heappush

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        # 출발지 위치 찾기
        if maps[i][j] == 'S':
            s1 = i; s2 = j
        # 목적지 위치 찾기
        elif maps[i][j] == 'F':
            f1 = i; f2 = j

heap = []
heappush(heap, (0, 0, s1, s2))
visited[s1][s2] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    cost, anw, x, y = heappop(heap)

    if x == f1 and y == f2:
        print(cost, anw)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 1차 4방향 탐색
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]== -1:
            if maps[nx][ny] == 'g':
                visited[nx][ny] = cost
                heappush(heap, (cost + 1, anw, nx, ny))
            
            elif maps[nx][ny] == '.':
                cnt = 0

                for j in range(4):
                    nnx = nx + dx[j]
                    nny = ny + dy[j]
                    # 2차 4방향 탐색 => 1차 4방향 탐색 + 4방향 탐색 시 쓰레기 옆을 지나가는 칸 탐색이 가능하다.
                    if 0 <= nnx < n and 0 <= nny < m:
                        if maps[nnx][nny] == 'g':
                            cnt += 1
                            
                # 1번이라도 쓰레기를 발견했다면 + 1
                if cnt > 0:
                    visited[nx][ny] = cost
                    heappush(heap, (cost, anw + 1, nx, ny))
                
                else:
                    visited[nx][ny] = cost
                    heappush(heap, (cost, anw, nx, ny))


            else:
                visited[nx][ny] = cost
                heappush(heap, (cost, anw, nx, ny))


