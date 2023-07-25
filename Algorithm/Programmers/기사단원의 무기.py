import math
def solution(number, limit, power):
    answer = 0
    result = []
    # 약수 개수 구하기
    for i in range(1, number+1):
        cnt = 0
        s = round(math.sqrt(i))
        for j in range(1, s + 1):
            if i % j == 0:
                cnt += 2
            if i / j == j:
                cnt -= 1
                
        result.append(cnt)

    for i in result:
        if i > limit:
            answer += power
        else:
            answer += i
    
    return answer