# 프로그래머스 / 숫자 문자열과 영단어

def solution(s):
    answer = s 
    answer = answer.replace('zero', '0')
    answer = answer.replace('one', '1')
    answer = answer.replace('two', '2')
    answer = answer.replace('three', '3')
    answer = answer.replace('four', '4')
    answer = answer.replace('five', '5')
    answer = answer.replace('six', '6')
    answer = answer.replace('seven', '7')
    answer = answer.replace('eight', '8')
    answer = answer.replace('nine', '9')


    return int(answer)

def solution(s):
    answer = s 
    num_s = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
        
    for item in num_s.items():                              # item()은 키와 값 쌍을 "튜플"로 반환하여 item에 넣어준다.
            answer = answer.replace(item[0], str(item[1]))  # 딕셔너리를 순회하며 입력값 중 영단어와 상응하는 값을 찾는다. 
                                                            # 튜플은 인덱스 0, 1로 이루어진 num_s의 키&값이므로 
                                                            # item[0]인 키('one;)와 상응하는 입력값을 item[1]인 값의 값('1')으로 바꾸어준다. 
                                                            # (one, 1) -> '14seveneight'
                                                            # 즉, item[0]가 상응하는 입력값을 인식하고, 이를 item[1]인 '1'로 바꾸어주는 기능


    return int(answer)