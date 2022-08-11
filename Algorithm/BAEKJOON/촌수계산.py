'''
input = 
9      -> 전체 사람 수
7 3    -> 찾을 촌수 계산 사람 번호
7      -> 관계 개수
1 2    -> 관계 번호 나열
1 3
2 7
2 8
2 9
4 5
4 6

output = 
3

시작을 7번으로 한다. 
'''

n = int(input())       
start, end = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]      # 인접 리스트를 넣어줄 리스트 생성
visited = [False] * (n + 1)             # 방문 여부 확인 리스트 생성

for _ in range(m):
    v1, v2 = list(map(int, input().split()))  # 노드값 넣어주기, list로 받아준다.
    graph[v1].append(v2)
    graph[v2].append(v1)

# 인접 노드 탐색
stack = []
stack.append((start, 0))                  # 촌수 계산을 같이 넣어준다.              
visited[start] = True               # 1번 노드를 True로 바꿔준다. 
    
answer = -1                         # 촌수 계산

while stack:                        # while len(stack) != 0: 스택이 비워있을 때 멈춘다.
    current, count = stack.pop()    # 스택에서 빠진 노드값이 current에 들어간다. 즉, 노드를 이동하는 역할이 된다.

    if current == end:            # pop한 값과 도달값이 같으면 멈춘다.
        answer = count
        break

    adj_graph = graph[current]      # 해당하는 값의 인접 그래프를 저장한다. 

    for adj in adj_graph:           # stack에서 제거된 노드값이 graph의 인덱스 위치가 된다. 인접 리스트 상에 포함된(연결된) 다른 노드 값을 adj에 하나씩 넣어준다.
            
        if not visited[adj]:        # 인접한 노드를 방문하지 않았다면
            visited[adj] = True     # True로 바꿔준다. 
            stack.append((adj, count + 1))       # 해당 노드값을 stack에 넣어준다. 
            
print(answer)


