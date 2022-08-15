# 완전 탐색 Exhaustive Search

## 

## Brute force

모든 경우의 수를 탐색하여 문제를 해결하는 방식이다.

가장 단순한 풀이 기법이며, **단순 조건문과 반복문**을 이용해서 풀 수 있다.

### 

### 예문 - 백준 2798 블랙잭

N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

N이 5이고, M이 21일때 5장의 카드 중 3장으로 21에 가깝게 조합한다. 



```python
n, m = map(int,input().split())                     
cards = list(map(int,input().split()))              # 카드의 값을 리스트로 받는다.
max_total = 0                                       # m에 가까운 최대치 값을 저장하기 위한 변수

for i in range(n - 2):                              
    for j in range(i + 1, n -1):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]

            if max_total < total <= m:              # 합산값이 이전 최대치보다 크거나 m(목표치)에 가까운 값이라면 
                max_total = total                   # 최대치 값이 된다.

            if total == m:                          # m(목표치)와 같다면
                max_total = total                   # 최대치로 저장한다.
                break

print(max_total)
```

3중 for문을 사용하여 3장의 카드를 조합한다. 

중복으로 뽑는 경우를 방지하기 위해 range 범위를 모두 다르게 설정하여 완전 탐색 시 모두 다른 범위를 탐색한다. 

## 

## Delta Search

이차원 리스트의 완전탐색에서 상하좌우를 탐색할 때 사용한다. 

행렬이 주어졌을 때 (0, 0)에서부터 이차원 리스트의 모든 원소를 순회하며, 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식이다.

![](https://blog.kakaocdn.net/dn/BnZM6/btrJCoplSQ6/aEK7A2KOL2JU0FZZYLAP6k/img.png)



행과 열의 변량인 -1, +1을 델타값이라 한다.

```python
(i + d[0], j + d[1])
```



상하좌우 이동 시 

```python
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 상하좌우 이동
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]


#범위를 벗어나지 않으면 갱신
if 0 <= nx < 3 and 0 <= ny < 3:
    x = nx
    y = ny
```

dx, dy에 리스트 형태로 상하좌우로 이동할 좌표값을 넣어준다. 

이후 반복문을 통해 nx, ny에 이동할 좌표값을 넣어준다. 

또한 이차원 리스트를 탐색할 때 범위를 벗어나지 않도록 설정한다. 

```python
# 상(x-1, y)
nx = x + dx[0]
ny = y + dy[0]
# 하(x+1, y)
nx = x + dx[1]
ny = y + dy[1]
# 좌(x, y-1)
nx = x + dx[2]
ny = y + dy[2]
# 우(x, y+1)
nx = x + dx[3]
ny = y + dy[3]
```

즉, 상하좌우로 탐색하는 방식은 dx, dy에 저장된 이동할 좌표값을 nx, ny에 넣어주며 이동하며 조건에 맞는 값을 탐색하는 것이다. 

```python
# 1. 델타값 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2. 이차원 리스트 순회
for x in range(n):
    for y in range(m):

        # 3.델타값을 이용해 상하좌우 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 4. 범위를 벗어나지 않으면 갱신
            if 0 <= nx < n and 0 <= ny < m:
                x = nx
                y = ny
```

기본적으로 이러한 방식으로 델타 탐색을 하게된다. 

```python
# 상, 하, 좌, 우, 좌상, 좌하, 우상, 우하
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]
```

또한, 상하좌우 뿐만 아니라 각 대각선 방향을 포함한 8방향을 탐색할 수 있다. 

```python
# 3.델타값을 이용해 8방향 이동
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
```

이때 기본 구문에서 nx, ny에 탐색 방향을 넣어줄 때 8방향을 탐색하므로 range를 8로 설정해야 한다.


