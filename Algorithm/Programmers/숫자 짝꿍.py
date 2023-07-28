from itertools import permutations
from collections import Counter
def solution(X, Y):
    answer = ''
    common = []
    
    x_cnt = Counter(X)
    y_cnt = Counter(Y)

    
    # 공통 수 탐색
    for i in y_cnt:
        if i in x_cnt:
            # 중복없이 공통의 수가 들어가게 됨
            common.append(i)

    # 공통 수 없을 경우     
    if not common:
        answer += '-1'
        return answer
    
    # 0밖에 없는 경우
    if common.count('0') == len(common):
        answer += '0'
        return answer

    chk = ''
    for i in common:
        # 더 작은 수를 할당
        if x_cnt[i] < y_cnt[i]:
            temp = x_cnt[i]
            for j in range(temp):
                chk += i
        else:
            temp = y_cnt[i]
            for j in range(temp):
                chk += i 

    result = sorted(chk, reverse=True)
    
    for i in result:
        answer += i

    return answer