'''
input = 
6 5
1 2
2 5
5 1
3 4
4 6

output = 
2

'''

n, m = map(int, input().split())        # 정점 개수(컴퓨터), 간선 개수(네트워크) 입력 
graph = [[] for _ in range(n + 1)]      # 인접 리스트를 넣어줄 리스트 생성
visited = [False] * (n + 1)             # 방문 여부 확인 리스트 생성

for _ in range(m):
    v1, v2 = map(int, input().split())  # 노드값 넣어주기
    graph[v1].append(v2)
    graph[v2].append(v1)

# 인접 노드 탐색
def dfs(start):
    stack = [start]                     # 1번 노드부터 시작하기 위해 적어준 구문. 이후 이 구문으로 오지 않는다.                 
    visited[start] = True               # 1번 노드를 True로 바꿔준다. 

    while stack:                        # while len(stack) != 0: 스택이 비워있을 때 멈춘다.
        current = stack.pop()           # 스택에서 빠진 노드값이 current에 들어간다. 즉, 노드를 이동하는 역할이 된다.

        for adj in graph[current]:      # stack에서 제거된 노드값이 graph의 인덱스 위치가 된다. 인접 리스트 상에 포함된(연결된) 다른 노드 값을 adj에 하나씩 넣어준다.
            if not visited[adj]:        # 인접한 노드를 방문하지 않았다면
                visited[adj] = True     # True로 바꿔준다. 
                stack.append(adj)       # 해당 노드값을 stack에 넣어준다. 

cnt = 0
for i in range(1, n + 1):               # start 설정
    if not visited[i]:                  # 만약 방문기록 리스트의 i번째가 True가 아니라면
        dfs(i)                          # i로 이동한다.
        cnt += 1                        # dfs에서 연결된 노드를 모두 탐색한 후 이 구문으로 돌아와 cnt에 +1 
print(cnt)
