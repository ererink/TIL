from collections import deque
def solution(priorities, location):
    answer = 1
    queue = deque(priorities)
    
    while True:
        if queue[0] < max(queue):
            if location != 0:
                queue.append(queue.popleft())
                location -= 1       # 앞으로 가게 되므로 
            else:                    # location이 0일 경우 맨 뒤로 가기 때문에
                location += len(queue) - 1
                queue.append(queue.popleft())
                
        elif queue[0] == max(queue):            # 최댓값이 맨 앞에 있을 경우
            if location != 0:                   # 찾을 인덱스값이 0이 아닐 경우
                location -= 1                   # 앞으로 이동
                answer += 1                     # 최댓값이 있다는 가정
                queue.popleft()                 # 최댓값 제거
            else:                               # 찾을 인덱스값이 0인 경우
                return answer
