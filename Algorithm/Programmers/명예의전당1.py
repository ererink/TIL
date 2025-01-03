from collections import deque

def solution(k, score):
    answer = []
    check = deque([])
    
    
    for i in score:
        if len(check) < k:
            check.append(i)
            
        else:
            if min(check) < i:
                check.popleft()
                check.append(i)
                
        check = deque(sorted(check))
        answer.append(min(check))
            
    return answer