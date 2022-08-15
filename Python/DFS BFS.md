# 깊이우선탐색(DFS), 너비우선탐색(BFS)



### 그래프 탐색 알고리즘이란?

**시작 정점에서 간선을 타고 이동**할 수 있는 모든 정점을 찾는 알고리즘이다. 

## 

## 깊이우선탐색  Depth First Search

**스택 + 그래프**

그래프의 깊이를 우선으로 탐색하기 위해 스택을 활용한다.

시작 정점부터 갈 수 있는 하위 정점까지 가장 깊게 탐색하고, 다시 마지막 갈림길로 돌아와 다른 정점을 탐색하여 모든 정점을 방문하여 순회한다. 

즉, 스택의 후입선출 기능을 통해 하위 정점까지 방문한 후 다시 마지막 갈림길로 돌아갈 때 스택에 마지막으로 저장해놓은 갈림길로 돌아갈 수 있는 것이다. 

이는 미로 탈출의 맥락과 같다. 탈출할 수 있는 길을 찾기위해 어느 한 쪽 길을 가장 깊게 들어갔다가 막히면 다시 돌아와 다른 길을 탐색하는 것이다. 

### 

### 깊이우선탐색 특징

모든 정점을 방문할 때 유리하다.

따라서 **경우의 수, 순열, 조합** 문제에서 많이 사용한다.

너비우선탐색에 비해 **코드 구현이 간단하다.**

단, 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우에는 너비우선탐색이 유리하다.

짧은 길을 찾고 더 이상 탐색하지 않을 때 유용하다. 

<img src="https://blog.kakaocdn.net/dn/MM9LL/btrJD4S38nK/ket7LZjiTcxOlIwLbIZvYk/img.png" title="" alt="" data-align="center">

### 동작 과정

그래프는 **인접 행렬** 혹은 **인접 리스트** 방식으로 표현할 수 있다.

노드를 방문한 것과 방문하지 않은 것을 구분하기 위해 Boolean으로 방문 체크 리스트를 생성한다. 



**DFS 사이클**

1. 현재 정점을 방문처리 한다.
2. 인접한 모든 정점을 확인한다. 
3. 방문하지 않은 인접한 정점으로 이동한다. 

### 

### 구현 방식

```python
graph = [
    [1, 2],
    [0, 3, 4],
    [0, 4, 5],
    [1],
    [1, 2, 6],
    [2],
    [4]
]

visited = [False] * n                 # 방문 처리 리스트 만들기

def dfs(start):
    stack = [start]                 # 돌아갈 곳을 기록
    visited[start] = True             # 시작 정점 방문 처리

    while stack:             # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
        current = stack.pop()         # 현재 방문 정점(후입선출)

        for adj in graph[current]:     # 인접한 모든 정점에 대해
            if not visited[adj]:     # 아직 방문하지 않았다면
                visited[adj] = True     # 방문 처리
                stack.append(adj)     # 스택에 넣기

dfs(0) # 0번 정점에서 시작
```

인접 리스트로 표현한 그래프를 기준으로 설명한다.



```python
visited = [False] * n # 방문 처리 리스트 만들기
```

일단 모두 방문하지 않은 상태로 False 값을 가진 방문 처리 리스트를 만들어준다. 



```python
dfs(0) # 0번 정점에서 시작

def dfs(start):
    stack = [start] # 돌아갈 곳을 기록
    visited[start] = True # 시작 정점 방문 처리
```

dfs 함수 하단에 0값을 넣어줌으로써 0번 노드부터 탐색을 시작하게 된다. 

0번은 현재 위치이므로 방문 처리 리스트 값을 True로 바꿔준다. 



```python
while stack: # 스택이 빌 때까지(돌아갈 곳이 없을때까지) 반복
    current = stack.pop() # 현재 방문 정점(후입선출)
```

while stack:은 while len(stack) != 0 :의 뜻과 같다. 

즉, 더 이상 stack에 값이 없을 때 까지 반복문을 실행한다. 

스택이 비워있을 때 while문은 멈추게 된다. 

stack에 값을 제거하면서 current 변수에 해당 값을 넣어준다. 

이 과정에서 인접한 노드로 이동하게 된다. 



```python
for adj in graph[current]: # 인접한 모든 정점에 대해
    if not visited[adj]: # 아직 방문하지 않았다면
        visited[adj] = True # 방문 처리
        stack.append(adj) # 스택에 넣기
```

이동한 현재 위치에 해당하는 (인접 리스트에서의) 인덱스 위치에 저장된 값(노드)들을 탐색한다.

if문을 통해 현재 위치의 노드가 방문 처리되지 않았다면, 

방문 처리 (True) 후 해당 값을 스택에 넣어준다.

이 과정을 반복하여 모든 노드를 방문하게 된다. 





## 너비우선탐색 Breadth-First Search

**큐 + 그래프**

시작 정점으로부터 가까운 정점을 먼저 방문하여 순차적으로 멀리있는 정점을 탐색하는 방식이다. 

최대한 넓게 이동하며, 더 이상 이동할 수 없을 때 아래로 이동한다. 

**순서대로** 탐색해야 하기 때문에 선입선출의 기능인 큐를 활용한다. 

BFS는 주로 최단거리를 구할 때 자주 사용한다. 

<img src="https://blog.kakaocdn.net/dn/d5ziSJ/btrJLToVB5M/KsKKoW09K1TvKsm8DbUnt1/img.png" title="" alt="" data-align="center">

### 

### 동작 과정

1. 탐색 시작 노드를 큐에 삽입하고 방문 처리한다.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리한다. 인접한 노드를 한 번에 큐에 삽입한다.
3. 2번의 과정을 수행할 수 없을 때까지 반복한다.

### 

### 구현 방식

```python
from collenctions import deque

def dfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in grahp[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```
