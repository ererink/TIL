import sys

t = int(input())
for test_case in range(1, t + 1):

    n, m = map(int, input().split())            # n = 사람의 수, m = 관계의 수
    graph = [[] for _ in range(n + 1)]      
    visited = [False] * (n + 1)             

    for _ in range(m):
        v1, v2 = map(int, input().split())  
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(start):
        stack = [start]
        visited[start] = True

        while stack:
            current = stack.pop()

            for moved in graph[current]:
                if not visited[moved]:
                    visited[moved] = True
                    stack.append(moved)

    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print('#{} {}'.format(test_case, cnt))

sys.stdin = open("_창용마을무리의개수.txt")
