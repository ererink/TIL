from itertools import combinations

def solution(number):
    answer = 0
    n = len(number)
    
    for i in combinations(number, 3):
        temp = 0
        for j in i:
            temp += j
        if temp == 0:
            answer += 1
            
    return answer