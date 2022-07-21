# 회문 검사
# 거꾸로 읽어도 제대로 읽은 것과 같은 문장과 낱말인 회문을 출력한다. 
# 입력 받아 회문이면 1을, 아니면 0을 출력한다. 

t = int(input())
for test_case in range(1, t + 1):

    word = str(input())
    palindrome = True

    for i in range(len(word) // 2):
        if word[i] == word[-1 -i]:
            print('#{} {}'.format(test_case, '1'))
            break
        else:
            print('#{} {}'.format(test_case, '0'))
            break


