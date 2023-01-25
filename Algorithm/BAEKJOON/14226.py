# 이모티콘

from collections import deque

S = int(input())
visited = [[-1] * (S + 1) for _ in range(S + 1)]
queue = deque()
queue.append((1, 0))
visited[1][0] = 0

while queue:
    screen, clip = queue.popleft()
    
    # 이모티콘이 목표 개수에 도달했을 때
    if screen == S:
        print(visited[screen][clip])
        break
    
    # 화면 -> 클립보드 저장
    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clip] + 1
        queue.append((screen, screen))
    
    # 클립보드 -> 화면 붙여넣기
    if screen + clip <= S and visited[screen + clip][clip] == -1:           # 화면과 클립보드의 이모티콘 개수가 S를 넘지 않을 경우로 범위를 지정해준다.
        visited[screen + clip][clip] = visited[screen][clip] + 1
        queue.append((screen + clip, clip))
        
    # 화면 이모티콘 1개 삭제
    if screen - 1 >= 0 and visited[screen - 1][clip] == -1:                 # 화면에서 이모티콘을 하나 삭제할 때 -가 될 경우를 방지하여 범위를 지정해준다.
        visited[screen - 1][clip] = visited[screen][clip] + 1
        queue.append((screen - 1, clip))
        
        