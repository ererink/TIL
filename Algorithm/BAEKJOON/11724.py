# DFS
import sys
input = sys.stdin.readline

n, m = map(int, input().split())            # 정점 개수, 간선 개수
graph = [[] for _ in range(n + 1)]          # 인접 리스트
visited = [False] * (n + 1)                 # 방문 여부

for _ in range(m):                          
    v1, v2 = map(int, input().split())      # 노드값 입력
    graph[v1].append(v2)                    # 인접 리스트에 번갈아가면서 넣기
    graph[v2].append(v1)

def dfs(start):                     
    stack = [start]                         # 1번 노드
    visited[start] = True                   

    while stack: # while len(stack) != 0:   # stack에 값이 없을 때 까지
        current = stack.pop()               # 현재 값은 stack에서 제거된 값

        for adj in graph[current]:          # graph에서의 현재 값
            if not visited[adj]:            # graph 현재 값이 방문되지 않았다면
                visited[adj] = True         # 방문한 값으로 변경하고
                stack.append(adj)           # 해당값을 stack에 넣어준다.

cnt = 0
for i in range(1, n + 1):                   # 1부터 n까지
    if not visited[i]:                      # 1부터 n까지의 인덱스 중 방문하지 않았다면
        dfs(i)                              # 함수에 넣어주고 탐색을 시작하도록 한다.
        cnt += 1                            # 연결된 노드의 탐색이 끝나고 해당 for문으로 도달했기 때문에
                                            # cnt에 1을 더한다. (한 노드의 덩어리)

print(cnt)