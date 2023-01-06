def solution(t, p):
    answer = 0
    check = ''
    l = len(p)
    
    for i in range(len(t)):
        check += t[i]
        if len(check) >= l:
            if check[-l:] <= p:
                answer += 1

    return answer