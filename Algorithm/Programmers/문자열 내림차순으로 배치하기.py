def solution(s):
    answer = ''
    temp = list(s)
    temp= sorted(temp, reverse=True)
    for i in temp:
        answer += i
    
    return answer