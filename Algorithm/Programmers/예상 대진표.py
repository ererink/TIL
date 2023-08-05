import math
def solution(n,a,b):
    answer = 1
    
    # 붙어있을 경우
    if a % 2 == 0:      # 짝수일 경우
        if b == (a - 1):
            return answer
    elif a % 2 == 1:    # 홀수일 경우
        if b == (a + 1):
            return answer
    
    q = round(math.sqrt(n))
    for i in range(q):
        answer += 1
        
        if a % 2 == 0:      # a가 짝수일 경우
            a = a // 2
        else:
            a = math.ceil(a / 2)
            
        if b % 2 == 0:
            b  = b // 2
        else:
            b = math.ceil(b / 2)
        
        # 같은 라운드인지 확인
        if a % 2 == 0:      # 짝수일 경우 b는 무조건 홀수여야함
            if b == (a - 1):
                return answer
        else:               # 홀수일 경우 b는 무조건 짝수
            if b == (a + 1):
                return answer
        
    return answer