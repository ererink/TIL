# 녹색 옷 입은 애가 젤다지?

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

MAX = sys.maxsize
print(MAX)
cnt = 0

# 입력값(n)이 0이 나올 때 까지 반복
while True:
    n = int(input())
    
    if n == 0:
        break
    
    maps = [list(map(int, input().rstrip().split())) for _ in range(n)]
    visited = [[MAX] * n for _ in range(n)]

    heap = []
    heappush(heap, (maps[0][0], 0, 0))  # 시작 좌표의 값과 좌표를 heap에 할당한다. (5, 0, 0) => rupee값을 맨 앞에 두어야 heap 정렬 시 rupee 기준으로 오름차순 정렬!
    visited[0][0] = maps[0][0]          # 시작 좌표의 값을 방문 리스트에 할당한다.

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    cnt += 1
    
    while heap:
        rupee, x, y = heappop(heap)
        
        # 현재 위치의 좌표값이 더해온 값보다 작으므로 
        if visited[x][y] < rupee:
            continue
        
        # (n, n)에 도착하면 중단
        if (x, y) == (n - 1, n - 1):
            print(f'Problem {cnt}: {rupee}')
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                # 4방향 탐색한 위치의 좌표값과 현재위치의 좌표값을 더해서 할당한다.
                n_rupee = rupee + maps[nx][ny]
                
                # 탐색한 좌표값과 현재위치 좌표값을 더한 값이 탐색한 좌표의 값보다 작을 때(최대수보다 작을 때)
                if visited[nx][ny] > n_rupee:   # 탐색하여 더한 누적된 최소비용 값이 이동하려는 값보다 작은 경우 이동
                    visited[nx][ny] = n_rupee   # 탐색 좌표값 + 현재 좌표값을 방문한 좌표에 할당
                    heappush(heap, (n_rupee, nx, ny))
            