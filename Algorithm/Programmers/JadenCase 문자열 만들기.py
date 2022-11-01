'''
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

"3people unFollowed me"	 
"3people Unfollowed Me"

'''

def solution(s):
    answer = ''
    s = s.lower()
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
        
        elif s[i - 1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer