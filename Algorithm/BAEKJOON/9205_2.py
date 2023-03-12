# 맥주 마시면서 걸어가기

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())    # 편의점 수
    s1, s2 = map(int, input().split()) # 출발지점 

    conven = []
    for i in range(n):  # 편의점 수 만큼 반복
        a, b = map(int, input().split())
        conven.append((a, b))

    e1, e2 = map(int, input().split()) # 도착지점 

    queue = deque()
    queue.append((s1, s2))
    visited = [False for k in range(n+1)]

    while queue:
        x, y = queue.popleft()

        if abs(x - e1) + abs(y - e2) <= 1000:
            print('happy')
            break

        for j in range(n):
            if visited[j] == False:
                nx, ny = conven[j]
                
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append((nx, ny))
                    visited[j] = True
    
    else:
        print('sad')