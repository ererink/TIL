# DFS와 BFS
# 방문 과정 출력

'''
4 5 1   => 정점의 개수, 간선의 개수, 탐색 시작 정점 번호
1 2
1 3
1 4
2 4
3 4
'''
import sys
from collections import deque

input = sys.stdin.readline


def dfs(v):
    visited_1[v] = True
    print(v, end=' ')

    for i in range(1, n + 1):
        if not visited_1[i]:
            dfs(i)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited_2[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(1, n + 1):
            if not visited_2[i]:
                visited_2[i] = True
                queue.append(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited_1 = [False] * (n + 1)
visited_2 = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(v)
print()
bfs(v)             






