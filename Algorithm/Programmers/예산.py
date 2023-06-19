def solution(d, budget):
    answer = 0
    n = len(d)
    d = sorted(d)     
    
    for i in d:
        if budget < i:
            break
        if n == 1:
            if budget > i:
                answer += 1
                break

        if budget < 0:
            answer -= 1
            break
        else:
            budget -= i
            answer += 1

    return answer