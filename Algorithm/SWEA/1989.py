# 회문 검사
# 거꾸로 읽어도 제대로 읽은 것과 같은 문장과 낱말인 회문을 출력한다. 
# 입력 받아 회문이면 1을, 아니면 0을 출력한다. 

t = int(input())
for test_case in range(1, t + 1):

    word = input()
    result = ''

    for i in range(len(word)-1, -1, -1): # 역순으로 i에 하나씩 넣는다.
        result += word[i]                # 정수가 아닌 word의 문자열로 역순된 
                                         # 값을 result에 하나씩 넣는다. 

    if result == word:                   # 역순된 값(result)와 원래의 값(word)를 비교한다.
        print('#{} {}'.format(test_case, '1'))
    else:                                # result와 word가 같지 않을 경우 '0'을 출력한다.
        print('#{} {}'.format(test_case, '0'))



