def solution(s):
    answer = ''
    
    # 홀수라면
    if len(s) % 2 == 1:
        answer = s[len(s) // 2] 
    
    else:
        answer += s[(len(s) // 2) - 1]
        answer += s[len(s) // 2 ] 
    
    return answer