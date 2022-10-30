'''
1-1. 입력된 수가 짝수라면 2로 나눕니다. 
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.
'''


def solution(num):
    answer = 0
    
    for i in range(500):
        if num == 1:
            return answer
            break
            
        if num % 2 == 0:
            num = num / 2
            answer += 1
        
        elif num % 2 == 1:
            num = (num * 3) + 1
            answer += 1
        
        
    if num != 1:
        return -1
