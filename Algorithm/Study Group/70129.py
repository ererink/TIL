def solution(x):
    answer = [0, 0]                     #[이진 변환 횟수, 제거한 0 개수]

    while True:                         # 특정 조건이 있으므로 
        if x == '1':                    # 입력값이 1일 경우 중단
            break
            
        answer[1] += x.count('0')       # 아닐 경우 입력값의 0을 센다. (즉 제거할 0의 개수이므로)
        x = x.replace('0', '')          # 0을 제거한다.
        length = len(x)                 # 제거한 후 문자열 길이를 측정한다. 
        x = bin(length)[2:]             # 문자열 길이를 이진 변환해준다.
        answer[0] += 1                  # 이진 변환 횟수 + 1
    
    return answer