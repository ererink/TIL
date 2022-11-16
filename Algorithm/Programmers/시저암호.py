'''
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 
예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 

s	    n	result
"AB"	1	"BC"
"z"	    1	"a"
"a B z"	4	"e F d"
'''
def solution(s, n):
    answer = ''
    for i in s:
        if i.islower():
            answer += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
            
        elif i.isupper():
            answer += chr((ord(i) - ord('A') + n) % 26 + ord('A'))
            # print(ord(i) - ord('A')) = 0
            # print(ord(i) - ord('A') + n) = 1
            # print((ord(i) - ord('A') + n) % 26) = 1
            # print((ord(i) - ord('A') + n) % 26 + ord('A')) = 66
            # print(chr((ord(i) - ord('A') + n) % 26 + ord('A'))) = B

        else:
            answer += ' '

    return ''.join(answer)