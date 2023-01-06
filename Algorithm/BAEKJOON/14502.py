# 연구소
'''
1. 벽 세우기
2. bfs로 바이러스 증식
3. 0 세기
4. 세운 벽 다시 0으로 돌려놓기

- combinations 사용하여 0이 최대한 많은 경우의 수 출력하기
'''

from collections import deque
import sys
import itertools
input = sys.stdin.readline

# 세로 가로
n, m = map(int, input().split())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

wall = 0
noninft = []
virus = []

for i in range(n):
    for j in range(m):
        
        # 0인 좌표 할당 (안전영역)
        if maps[i][j] == 0:
            noninft.append((i, j))
        
        # 2인 좌표 할당 (바이러스)
        elif maps[i][j] == 2:
            virus.append((i, j))
        
        else:
            wall += 1

noninft3 = []
# 경우의 수, 3개로 조합
for j in itertools.combinations(noninft, 3):
    noninft3.append(j)

dx = [0, 0, -1, 1]
dy = [1, -1, 0 , 0]


# 바이러스 증식
def bfs():
    now = deque()
    visit = [[0] * m for _ in range(n)]
    
    for i in virus:
        now.append(i)
        visit[i[0]][i[1]] = 2
    
    while now:
        x, y  = now.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 0 and visit[nx][ny] == 0:
                    # 바이러스 증식
                    visit[nx][ny] = 2
                    now.append((nx, ny))
    
    cnt = 0
    # 안전영역 구하기
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0:
                cnt += 1
    
    return cnt - wall - 3

result = []
for i in noninft3:
    # 벽 세우기
    for j in i:
        maps[j[0]][j[1]] = 1
    result.append(bfs())
    
    # 세운 벽 원상복귀
    for j in i:
        maps[j[0]][j[1]] = 0

print(max(result))