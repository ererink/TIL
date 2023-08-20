def solution(clothes):
    answer = 1
    n = len(clothes)
    clo_dict = {}
    for i in range(n):
        if clothes[i][1] in clo_dict:
            clo_dict[clothes[i][1]] += 1
        else:
            clo_dict[clothes[i][1]] = 1
    
    for k, v in clo_dict.items():
        answer *= (v+1)
    return answer - 1