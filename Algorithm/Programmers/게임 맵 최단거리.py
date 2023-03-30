from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0] * m for _  in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            answer = visited[x][y]
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    else:
        answer = -1     
    return answer