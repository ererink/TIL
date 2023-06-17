def solution(n):
    answer = ''
    even = '수'
    odd = '박'
    
    for i in range(n):
        if i % 2 == 0:
            answer += even
        else:
            answer += odd
    return answer