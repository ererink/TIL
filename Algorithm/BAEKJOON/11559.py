# Puyo Puyo

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def search(a, b, clear):
    queue = deque()
    queue.append((a, b))
    visited = [[False] * 6 for _ in range(12)]  # 
    puyo = 1
    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny]:
                # 같은 색의 뿌요 찾기
                if maps[nx][ny] == maps[x][y]:
                    puyo += 1                               # 같은 색의 뿌요 카운트
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    if puyo >= 4:                                           # 같은 색의 뿌요가 4개 이상일 경우
        clear += 1                                          # 터트린 횟수 카운트
        for i in range(12):
            for j in range(6):
                if visited[i][j] == True:                   # 뿌요가 있었던 곳 (같은 색의 뿌요를 탐색하고 방문했다면)
                    maps[i][j] = '.'                        # 해당 뿌요를 터트린다
                
    return clear
    
def gdown():
    for i in range(10, -1, -1):                             # 뿌요들은 아래 행에 존재하기 때문에 10부터 0까지 탐색 (11이 아닌 이유는 맨 아래행에 가지 못하는 뿌요를 바로 윗칸에 배치하기 위해)
        for j in range(6):
            if maps[i][j] != '.' and maps[i + 1][j] == '.':  # 아래 행이 비어있을 때
                
                for k in range(i+1, 12):
                    if k == 11 and maps[k][j] == '.':       # 가장 아래쪽 행에 뿌요가 없다면
                        maps[k][j] = maps[i][j]             # 뿌요를 가장 아래쪽 행으로 옮기기
                    elif maps[k][j] != '.':                 # 가장 아래쪽 행으로 옮길 수 없다면
                        maps[k-1][j] = maps[i][j]           # 바로 윗칸에 두기
                        break
                maps[i][j] = '.'                            # 현재 위치의 뿌요 없애기 (이미 옮겼으므로)

maps = [list(input()) for _ in range(12)]

asw = 0
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if maps[i][j] != '.':
                cnt = search(i, j, cnt)

    if cnt == 0:    # 더 이상 터트릴 뿌요가 없다면
        print(asw)  # 터트린 횟수 출력
        break
    else:
        asw += 1    # 터트린 횟수 카운트
    gdown()         # 터트린 후 뿌요들은 가장 아래의 행으로 내려가도록 한다.