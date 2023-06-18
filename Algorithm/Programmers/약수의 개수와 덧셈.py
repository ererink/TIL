def solution(left, right):
    answer = 0
    
    for i in range(left, right + 1):
        temp = []
        for j in range(1, i + 1):
            if i % j == 0:
                temp.append(j)
                temp.append(i//j)
                
        # 중복된 약수 빼기
        temp = set(temp)
        # 약수의 개수가 짝수라면
        if len(temp) % 2 == 0:
            # 현재 반복문의 숫자 더하기
            answer += i
        # 약수의 개수가 홀수라면
        else:
            # 현재 반복문의 숫자 빼기
            answer -= i
            
    return answer