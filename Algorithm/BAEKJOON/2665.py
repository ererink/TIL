# 미로만들기

from heapq import heappop, heappush
import sys

INF = sys.maxsize

n = int(input())
maps = [list(map(int, input())) for _  in range(n)]
visited = [[INF] * n for _ in range(n)]

heap = []
heappush(heap, (0, 0, 0))
visited[0][0] = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while heap:
    cost, x, y = heappop(heap)

    if x == n - 1 and y == n - 1:
        print(cost)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            # 검은방일 경우
            if maps[nx][ny] == 0:
                new_cost = cost + 1
            
            # 흰방일 경우 그냥 이동
            else:
                new_cost = cost
            
            if visited[nx][ny] > new_cost:
                visited[nx][ny] = new_cost
                heappush(heap, (new_cost, nx, ny))