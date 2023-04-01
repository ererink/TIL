from collections import deque
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(search(i, j, visited, maps, n, m))
    
    if answer:
        return sorted(answer)
    else:
        answer.append(-1)
        return answer
    
def search(a, b, visited, maps, n, m):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    cnt = int(maps[a][b])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] != 'X':
                    cnt += int(maps[nx][ny])
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return cnt