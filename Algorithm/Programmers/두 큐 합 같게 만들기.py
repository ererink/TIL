from collections import deque
def solution(queue1, queue2):
    answer = 0
    n = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    q1 = 0; q2 = 0

    for i in range(n):
        q1 += queue1[i]
        q2 += queue2[i]

    while q1 != q2:
        if q1 > q2:
            temp = queue1.popleft()
            q1 -= temp
            q2 += temp
            queue2.append(temp)
            answer += 1
            
        elif q1 < q2:
            temp = queue2.popleft()
            q1 += temp
            q2 -= temp
            queue1.append(temp)
            answer += 1
        
        if q1 == 0 or q2 == 0:
            answer = -1
            break
    return answer