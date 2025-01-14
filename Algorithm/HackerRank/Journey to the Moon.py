from collections import deque

def journeyToMoon(n, astronaut):
    answer = []
    graph = [[] for _ in range(n)]
    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    country_sizes = []    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        size = 1
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    size += 1
        return size
    
    for j in range(n):
        if not visited[j]:
            country_sizes.append(bfs(j))
     
    total = n * (n - 1) // 2
    same_country = 0
    for i in country_sizes:
        same_country += (i * (i - 1)) // 2
    
    return total - same_country