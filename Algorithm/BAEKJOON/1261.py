# 알고스팟
from heapq import heappop, heappush
import sys

n, m = map(int, input().split())
maps = [list(map(int, input())) for _ in range(m)]

MAX = sys.maxsize
visited = [[MAX] * n for _ in range(m)]


heap = []
heappush(heap, (0, 0, 0))
visited[0][0] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    wall, x, y = heappop(heap)
    
    if (x, y) == (m - 1, n - 1):
        print(wall)
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < m and 0 <= ny < n:
            if maps[nx][ny] == 1:
                breaking = wall + 1
            
            # 0일 경우 누적 횟수를 그대로 옮겨줘야 한다.
            else:
                breaking = wall
            
            if visited[nx][ny] > breaking:
                visited[nx][ny] = breaking
                heappush(heap, (breaking, nx, ny))