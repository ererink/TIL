'''
a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b의 대소관계는 정해져있지 않습니다.

a	b	return
-------------
3	5	12
3	3	3
5	3	12
'''

def solution(a, b):
    answer = 0
    
    if a > b:
        for i in range(b, a + 1):
            answer += i
    
    elif a < b:
        for i in range(a, b + 1):
            answer += i
    
    else:
        answer = a
    return answer