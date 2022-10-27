# 런파일 에러난 접근법
'''
my_string을 계산한 결과값은 1 이상 100,000 이하.
계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수.
'''
def solution(my_string):
    answer = 0
    num = ''
    
    for i in my_string:
        if i == ' ':
            continue
        elif i == '+':
            answer += int(num)
            num = ''
        else:
            num += i
    
    answer += int(num)
    return answer

# 내장함수 사용
def solution(my_string):
    return eval(my_string)