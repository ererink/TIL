'''
햄버거 만들기

ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.

ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]	
result = 2
'''

def solution(ingredient):
    answer = 0
    order = [1, 2, 3, 1]
    check = []
    
    for i in ingredient:
        check.append(i)
        if check[-4:] == order:
            answer += 1
            for j in range(4):
                check.pop()
    
    return answer