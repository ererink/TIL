
n = int(input()) # 정점 개수(컴퓨터)
m = int(input()) # 간선 개수(네트워크)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)             # 방문 여부 확인 리스트 생성

# 인접 리스트 만들기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 인접 노드 탐색
def dfs(start):
    stack = [start]                     # 1번 노드부터 시작하기 위해 적어준 구문. 이후 이 구문으로 오지 않는다.                 
    visited[start] = True               # 1번 노드를 True로 바꿔준다. 

    while stack:                        # while len(stack) != 0: 스택이 비워있을 때 멈춘다.
        current = stack.pop()           # 스택에서 빠진 노드값이 current에 들어간다.

        for adj in graph[current]:      # 빠진 노드가 인접 리스트 상에 포함된(연결된) 다른 노드 값을 adj에 하나씩 넣어준다.
            if not visited[adj]:        # 인접한 노드를 방문하지 않았다면
                visited[adj] = True     # True로 바꿔준다. 
                stack.append(adj)       # 해당 노드값을 stack에 넣어준다. 
dfs(1)                                  # 1번 노드부터 시작하게 해준다. 

print(visited.count(True) - 1)          # 맨 처음 시작했던 1번 노드는 빼준다. 