from collections import deque

def roadsAndLibraries(n, c_lib, c_road, cities):
    # 모든 도시에 도서관을 짓는 것이 더 저렴한 경우
    if c_lib <= c_road:
        return n * c_lib

    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)
    print(graph)

    visited = [False] * (n + 1)
    total_cost = 0

    def bfs(start):
        queue = deque([start])
        visited[start] = True
        size = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    size += 1
        return size

    for city in range(1, n + 1):
        if not visited[city]:
            component_size = bfs(city)
            # 최소 비용 계산
            total_cost += c_lib + (component_size - 1) * c_road

    return total_cost

n = 3
c_lib = 2
c_road = 1
cities = [[1, 2], [3, 1], [2, 3]]
answer = roadsAndLibraries(n, c_lib, c_road, cities)