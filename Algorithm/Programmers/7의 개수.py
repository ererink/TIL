def solution(array):
    answer = 0
    
    for i in array:
        answer += (str(i).count('7'))
    return answer