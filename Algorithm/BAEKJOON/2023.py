# 신기한 소수
# DFS 

'''
슈도코드
n 자릿수

1. 소수 구하기 함수 
for i를 2부터 현재 수/2+1까지 반복:
    if 현재 수 % i 가 0이면:
        return 소수가 아님

2. DFS 
dfs(숫자):
    if 자릿수 == n:
        현재 수 출력
    else:
        for i를 1부터 9까지 반복:
            if i를 뒤에 붙인 새로운 수가 홀수이면서 소수일 때 
            dfs(수 * 10 + 뒤에 붙는 수) 실행한다.

dfs 실행(숫자 2, 3, 5, 7로 탐색 시작)
'''
n = int(input())

def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    
    return True

def dfs(number):
    if len(str(number)) == n:
        print(number)
    
    else:
        for i in range(1, 10):
            if i % 2 == 0:              # 짝수면 탐색하지 않는다.
                continue
            if isPrime(number * 10 + i): # 소수이면 자릿수를 늘린다.
                dfs(number * 10 + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)