def solution(s):
    answer = 0
    x1 = 0
    x2 = 0
    
    for i in s:
        if x1 == x2:        # 먼저 카운트한 문자열과 다른 문자열을 카운트한 횟수가 같으면 문자열을 나눈다.
            answer += 1
            x = i
            
        if x == i:          # 앞 문자열과 다음 문자열이 같아면 카운트 + 1
            x1 += 1
        else:
            x2 += 1         # 다른 문자열이면 x2 카운트 + 1
            
    return answer           # 나눈 문자열 출력