from collections import deque
import sys

input = sys.stdin.readline

def bfs():
  queue = deque()
  queue.append(start)
  visited = [False]*n    #편의점의 수만큼 방문 여부를 체크하

  while queue:
    x,y = queue.popleft()
    if abs(x-end[0])+ abs(y-end[1]) <= 1000:    #목적지와 현재 위치의 거리가 1000이하 (20*50)라면,
      return True    
    for i in range(n):    #편의점의 개수만큼 반복
      if visited[i] == False:    #i번째 편의점을 방문하지 않았다면,
        
        nx,ny =data[i]    #편의점의 좌표를 nx,ny에 저장
        if abs(x-nx)+abs(y-ny)<=1000:    #현재위치와, 편의점의 위치의 거리가 1000이하라면,
          visited[i] = True    #방문 처리를 하고,
          queue.append([nx,ny])    #큐에 편의점의 위치를 추가.
  return False    #중간에 True가 리턴되지 않는경우, 거리가 1000을 초과하는 경우, False 리턴


t = int(input())    #테스트 케이스의 수

for _ in range(t):
  n = int(input())    #편의점의 수
  data = []
  start = list(map(int,input().split()))    #출발할 집의 좌표
  for _ in range(n):
    data.append(list(map(int,input().split())))    #편의점의 좌표를 수만큼 입력
  end = list(map(int,input().split()))    #목적지의 좌표
  result = bfs()    #bfs함수의 반환값을 result변수에 저장
  if result:    #result가 True이면,
    print('happy')
  else:    #result가 True가 아니라면,
    print('sad')