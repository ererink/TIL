def solution(s):
    answer = 0
    chk = []
    
    # 빈 문자열일 경우
    if not s:
        return 0
    
    # 홀수일 경우
    if len(s) % 2 != 0:
        return 0
    
    for i in s:
        chk.append(i)
        if len(chk) > 1 and chk[-1] == chk[-2]:
            chk.pop()
            chk.pop()
            
    if chk:
        answer = 0
    else:
        answer = 1
        
    return answer
