def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    s = s.lower()
    
    p_cnt = s.count('p')
    y_cnt = s.count('y')
    
    if p_cnt != y_cnt:
        answer = False
        
    return answer