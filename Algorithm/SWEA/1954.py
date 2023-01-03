'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

input = 2    
        3   
        4
        
output = #1
        1 2 3
        8 9 4
        7 6 5
        #2
        1 2 3 4
        12 13 14 5
        11 16 15 6
        10 9 8 7

- 벽에 부딪히면 방향 바꾸기 (우, 하, 좌, 상 순서 반복)
'''
from collections import deque

dx = [0, 1, 0, -1]      # 우 하 좌 상
dy = [1, 0, -1, 0]

t = int(input())

for testcase in range(1, t + 1):
    n = int(input())
    maps = [[0] * n for _ in range(n)]
    queue = deque([(0,0)])
    start = 1                   # 처음 위치
    turn = 0                    # 방향 돌기
    maps[0][0] = 1              # 처음 위치를 1로 시작

    while queue:
        x, y = queue.popleft()      
        
        nx = x + dx[turn]
        ny = y + dy[turn] 
        # 다 돌았을 경우 멈추기
        if start == n * n:
            break

        # 범위에 있고, 값이 0인 좌표
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 0:
            start += 1                      # 좌표 이동
            maps[nx][ny] = start            # 이동하면서 1씩 커지는 좌표값
            queue.append((nx, ny))

        # 방향을 바꿀 때
        else:            
            turn = (turn + 1) % 4
            queue.append((x, y))
    
    print(f'#{testcase}')
    
    for i in maps:
        print(*i)