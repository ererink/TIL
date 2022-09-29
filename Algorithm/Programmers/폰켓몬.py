# 딕셔너리.ver

def solution(nums):
    answer = 0
    result = {}
    for key in nums:
        if key not in result:
            result[key] = 1
        else:
            result[key] += 1
            
    if len(nums) // 2 >= len(result.keys()):
        answer =  len(result.keys())

    else:
        answer = len(nums) // 2 
        
    return answer