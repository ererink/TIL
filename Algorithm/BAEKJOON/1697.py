# 숨바꼭질
# BFS
'''
1. 큐를 빠르게 해 주기 위해 q = deque()를 설정해주었다.
2. 그다음 첫 번째, 수빈이가 있는 위치 N(출발점)을 넣어준다.
3. while문을 돌려 q가 정수일 때 계속 반복시켜준다.
4. 제일 왼쪽 값을 pop, 그리고 그 값을 x에 저장
5. 만약 그 x의 값이 동생이 있는 위치 k일시 dist [x]를 출력하고 프로그램 종료
6. for문을 돌린다. x-1, x+1, x*2의 값을 j에 순서대로 넣어준다.
7. 만약 j의 값이 0과 MAX 사이의 값이고 dist [j]가 0의 값을 가질 시 dist [x]+1을 해주고 j를 추가
8. 값을 찾을 때까지 반복
'''
import sys
from collections import deque
input = sys.stdin.readline()

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()

        if x == k:
            print(dist[x])
            break
    
        for j in (x - 1, x + 1, x * 2):
            if 0 <= j <= MAX and not dist[j]:
                dist[j] = dist[x] + 1
                queue.append(j)

MAX = 100000
n, k = map(int, input.split())
dist = [0] * (MAX + 1)

bfs()