def solution(a, b, n):
    answer = 0    
    
    while n >= a:        
        # 최대 배수 구하기
        max_num = (n // a) * a                    
        cola = (max_num // a) * b
        answer += cola
        
        if n - max_num >= 1:  
            n = cola + (n - max_num)
        else:
            n = cola
            
    return answer