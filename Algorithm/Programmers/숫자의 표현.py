def solution(n):
    answer = 0
    chk = 0
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            chk += j
            if chk == n:
                answer += 1
                chk = 0
                break
            elif chk > n:
                chk = 0
                break
            
    return answer