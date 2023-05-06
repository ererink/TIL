# 경로 찾기

from collections import deque
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def search(a):
    queue = deque()
    queue.append(a)
    visited = [0 for _ in range(n)]     # 열 검사

    while queue:
        x = queue.popleft()             # 행 탐색

        for i in range(n):              # 열 탐색
            if visited[i] == 0 and maps[x][i] == 1:
                queue.append(i)         # 현재 열 할당 => x를 통해 행으로 변환 (대칭 행렬이므로)
                visited[i] = 1
                result[a][i] = 1
            
for i in range(n):
    search(i)                           # 행 탐색 

for i in result:
    print(*i)

    