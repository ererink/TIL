# 치즈
from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

cnt = 0

while True:
    visited = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    melting = {}                            # 좌표를 (a, b): 1 형식으로 넣고 두 변 이상 맞닿아 있을 경우 0으로 처리

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if maps[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                
                # 치즈가 있는 경우
                else:
                    # 해당 좌표가 딕셔너리에 없다면
                    if (nx, ny) not in melting:
                        # 새로 딕셔너리에 추가
                        melting[(nx, ny)] = 1
                    
                    # 이미 좌표가 있다면
                    else:
                        # 해당 Key에 1을 추가
                        melting[(nx, ny)] += 1

    # 딕셔너리에 아무것도 담기지 않았다면 while True문 중단 => 더 이상 녹을 치즈가 없음
    if len(melting) == 0:
        break   
    
    # 딕셔너리에 값들이 담겨있다면
    else:
        # k에는 key값, v에는 value값 할당
        for k, v in melting.items():
            # 좌표가 두번 이상 들어갔다면
            if v >= 2:
                maps[k[0]][k[1]] = 0        # 해당 키값의 좌표(x, y)를 0으로 만든다 => 두변 이상 맞닿았기 때문에 치즈가 녹음
        
        cnt += 1    # for문이 끝날 때마다 치즈가 녹는 한시간이 지나므로 1을 더해줌

print(cnt)
