'''
안전 영역

어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램을 작성하시오. 

input = 5
        6 8 2 6 2
        3 2 3 4 6
        6 7 3 3 2
        7 2 5 3 6
        8 9 5 2 7

output = 5
'''

from collections import deque

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
maxn = 0    # 영역 중 최대 높이 구하기

for i in range(n):
    for j in range(n):
        if maps[i][j] > maxn:
            maxn = maps[i][j]   # 영역 중 최대 높이 구하기

dx = [0, 0, 1, -1]	# 우 좌 하 상
dy = [1, -1, 0, 0]

def bfs(a, b, k, visit):
    queue = deque()
    queue.append((a, b))
    visit[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                if maps[nx][ny] > k:
                    visit[nx][ny] = True
                    queue.append((nx, ny))


max_land = 0
for k in range(maxn): # 0부터 최대 높이까지 각 높이의 영역 탐색
    visit = [[False] * n for _ in range(n)]
    land = 0
    
    for i in range(n):
        for j in range(n):
            if maps[i][j] > k and not visit[i][j]:  # k를 통해 각 높이 영역 탐색
                bfs(i, j, k, visit)
                land += 1
    
    if max_land < land: # 최종 최대 영역 구하기
        max_land = land
    
print(max_land)