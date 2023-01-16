# 빙산

import sys
input = sys.stdin.readline
n ,m = map(int, input().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

year = 0
# 가장 큰 값이 존재할 때 까지 반복
while max(map(max, maps)):
    iceberg = [[0] * m for _ in range(n)]

    # 0만큼 빙산깎기
    # for문을 통해 x, y변수를 주어 4방향 탐색이 끝난 후 다른 빙산 좌표로 이동하게 됨
    for x in range(n):
        for y in range(m):
            if maps[x][y] != 0:
                z_cnt = 0

                # 4방향 탐색
                for q in range(4):
                    nx = x + dx[q]
                    ny = y + dy[q]

                    if 0 <= nx < n and 0 <= ny < m:
                        if maps[nx][ny] == 0:
                            # 인접한 0(빈칸) 수 세기
                            z_cnt += 1

                # 4방향을 모두 방문한 후 0개수 만큼 빙산 값을 빼기
                # 0보다 작으면 방문기록에 0으로 표시
                if maps[x][y] - z_cnt < 0: 
                    iceberg[x][y] = 0
                else:
                    iceberg[x][y] = maps[x][y] - z_cnt
    
    # 분리된 빙산 찾기
    visit = [[False] * m for _ in range(n)]
    land = 0
    for x in range(n):
        for y in range(m):
            if iceberg[x][y] != 0 and not visit[x][y]:
                visit[x][y] = True
                queue = [(x, y)]
                land += 1

                # 하나의 빙산 탐색
                while queue:
                    a, b = queue.pop()

                    for w in range(4):
                        nx = a + dx[w]
                        ny = b + dy[w]

                        if 0 <= nx < n and 0 <= ny < m:
                            if iceberg[nx][ny] != 0 and not visit[nx][ny]:
                                visit[nx][ny] = True
                                queue.append((nx, ny))

    if year == 0 and land >= 2:
        print(year)
        break
    # 조건이 충족되지 않으면 다시 while문 반복
    year += 1  
                              
    if land >= 2:
        print(year)
        break
        
    maps = iceberg
else:
    print(0)


'''
특이사항
- 분리된 빙산을 찾을 때 nx, ny의 범위를 확인하고 iceberg가 0이 아닌 좌표값을 확인할 때

if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
    if iceberg[nx][ny] != 0 :

으로 작성할 때는 런타임 에러가 났고, 이를 현재 코드로 작성하니 오류 해결함
'''