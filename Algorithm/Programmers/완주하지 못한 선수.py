# 딕셔너리.ver
def solution(participant, completion):
    result = {}
    answer=''    
    for key in participant:
        if key not in result:
            result[key] = 1
        else:
            result[key] += 1
    
    for key in completion:
        result[key] -= 1
    
    for key in result:
        if result[key] >= 1:
            answer = key
            break
    return answer