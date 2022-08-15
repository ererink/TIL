# 그래프 graph



### 그래프란?

**정점(vertex**)과 이를 연결하는 **간선(edge)** 들의 집합으로 이루어진 비선형 자료구조이다.

ex) 소셜 네트워크, 지하철 노선도

- 정점(vertex): 간선으로 연결되는 객체, 노드(node)라고도 한다.
- 간선(edge): 정점 간의 관계(연결)를 표현하는 선
- 경로(path): 시작 정점부터 도착 정점까지 거치는 정점
- 인접(adjacency): 두 개의 정점이 하나의 간선으로 직접 연결된 상태

## 

## 그래프의 종류

**무방향 그래프 (Undirected graph)**

- 간선의 방향이 없는 가장 일반적인 그래프이다. 
- 간선을 통해 양방향의 정점 이동 가능하다. 
- **차수 Degree:** 하나의 정점에 연결된 간선의 개수이다. 
- 모든 정점의 차수의 합 = 간선 수 * 2

<img title="" src="https://blog.kakaocdn.net/dn/bNUbeO/btrJAQtlRec/4kIKjcwWmfISLwVysi0Khk/img.png" alt="" width="573" data-align="center">



**유방향 그래프 (Directed graph)**

- 간선의 방향이 있는 그래프이다. 
- 간선의 방향이 가리키는 정점으로 이동한다. 
- **차수 Degree:**: 진입 차수와 진출 차수로 나누어진다. 

<img src="https://blog.kakaocdn.net/dn/biwvDo/btrJAeuZ120/ERg3EBO8btQfBIgBl16B8K/img.png" title="" alt="" data-align="center">



## 그래프의 표현

### 인접 행렬 Adjacent matrix

두 정점을 연결하는 간선이 없으면 0, 있으면 1을 가지는 행렬로 표현하는 방식이다. 

<img src="https://blog.kakaocdn.net/dn/r82Lk/btrJBFZaNFo/WK4oyKI9no1LuIAzqU5ovk/img.png" title="" alt="" data-align="center">

(Image from cs.mtsu.edu)



각 행, 열에서 0, 0의 값인 0을 기준으로 대칭을 이루고 있다. 

```python
'''input =     0 1    0 2    1 3    1 4    2 4    2 5    4 6'''

n = 7 # 정점 개수
m = 7 # 간선 개수

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
```

먼저 [0]으로 n X m 행렬을 만들어준다 

반복문을 통해 차례대로 값을 받는다.

```python
graph[v1][v2] = 1
graph[v2][v1] = 1
```

무방향 그래프이므로 0의 위치에 1을 넣어주고, 1의 위치에 0을 차례대로 넣어준다. 

```python
# 인접 행렬 결과

graph = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]
 ]
```

### 



### 인접 리스트

리스트를 통해 각 정점에 대한 인접 정점들을 순차적으로 표현하는 방식이다. 

<img title="" src="https://blog.kakaocdn.net/dn/buwXHe/btrJACCCMLM/ayZEajRl2nThEed48UkMRk/img.jpg" alt="" width="580" data-align="center">

(image from lavivienpost.net)

```python
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4, 5],
    3: [1],
    4: [1, 2, 6], 
    5: [2],
    6: [4]
}
```

인접 리스트는 0부터 6까지 인덱스 위치에 각 인접하는 노드의 값이 리스트 형태로 들어가게 된다. 



```python
n = 7 # 정점 개수
m = 7 # 간선 개수

graph = [[] for _ in range(n)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
```

빈 리스트를 행 개수만큼 만들어준다. 

인접 행렬과 마찬가지로 각 해당하는 인덱스 위치에 인접한 노드의 값을 (v1 - v2) 넣어준다. 



```python
graph = {
    [1, 2],
    [0, 3, 4],
    [0, 4, 5],
    [1],
    [1, 2, 6], 
    [2],
    [4]
}       
graph[0][0] => 1
```

위 구문을 통해 이러한 인접 리스트를 생성할 수 있다. 

즉, graph[0][0]을 탐색한다면 1의 값을 출력하게 된다. 

인접 행렬은 직관적이고 만들기 편하지만 불필요하게 공간이 낭비되는 단점이 있다.

인접 리스트는 연결된 정점만 저장하여 인접된 상태만 보기 때문에 효율적이므로 자주 사용된다.
