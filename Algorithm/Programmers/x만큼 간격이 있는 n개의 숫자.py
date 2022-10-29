def solution(x, n):
    answer = []
    cnt = x
    
    for i in range(n):
        answer.append(cnt)
        cnt += x
    return answer