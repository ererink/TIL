s = list(input())
answer = ''                         # 정답 바로 출력 (뒤집지 않는다)
stack = ''                          # 뒤집어야 할 문자열 넣기
flag = 0 

for i in s:
    if flag == 0:
        if i == '<':                    # 답안에 그대로 넣기
            flag = 1
            answer += stack[::-1]
            stack = ''
            answer += i
            continue
    
        elif i == ' ':
            answer += stack[::-1]
            answer += i
            stack = ''
    
    
        else:                           # 아무런 조건에 부합되지 않는 경우, 뒤집어야 할 경우
            stack += i                  # 뒤집어주기 위해 stack에 넣는다.

    if flag == 1:
        answer += i
        if i == '>':
            flag = 0
        
answer += stack[::-1]
stack = ''
print(answer)