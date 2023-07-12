def solution(k, score):
    answer = []
    check = []
    for i in score:
        check.append(i)
        
        # 첫번째 비교
        if len(check) == k:
            answer.append(min(check))
        
        elif len(check) > k:
            check = sorted(check, reverse=True)
            check.pop()
            answer.append(min(check))
            
        else:
            answer.append(min(check))
            
    return answer