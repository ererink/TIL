def solution(k, tangerine):
    answer = 0
    tan_dict = {}
    
    for i in tangerine:
        # 딕셔너리에 없으면 생성
        if i not in tan_dict:
            tan_dict[i] = 1
        # 있으면 개수 + 1
        else:
            tan_dict[i] += 1
    
    tan_dict = sorted(tan_dict.items(), key = lambda x: x[1])
    
    while k > 0:
        k -= tan_dict.pop()[1]
        answer += 1
    return answer