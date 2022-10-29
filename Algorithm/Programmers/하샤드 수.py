def solution(x):
    answer = True
    cal = 0
    
    for i in str(x):
        cal += int(i)
    
    if x % cal != 0:
        answer = False
    
    return answer