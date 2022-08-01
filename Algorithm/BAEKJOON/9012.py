# 내 답안

# 다른 답안
n = int(input())                        # 반복 횟수 입력값

for i in range(n):                      # n만큼 반복
    stack = []                          # 임시적으로 담아줄 리스트 (소괄호가 완성되면 삭제)
    line = input()                      # 소괄호 입력값
    for item in line:                   # 입력값을 하나씩 변수 item에 옮긴다
        if stack:                       # 무조건 소괄호 하나를 stack 리스트에 넣는다
            if item =='(':              
            
                stack.append(item)      # '('를 stack에 넣는다
                
            elif item==')':             # ')' 라면
                if stack[-1]=='(':      # 마지막에 넣은 값이 '(' 라면
                    stack.pop()         # '(' 를 뺀다
                                        # ')'를 넣지 않아도 이미 짝을 이루기 때문에 stack 리스트에 담겨진 '('를 삭제한다
                    
                else:
                    stack.append(item)  # '(' 가 아니라면 ')'를 넣어준다 ([ ), )  ])
                
        else:
            stack.append(item)          # 무조건 소괄호 하나를 stack 리스트에 넣는다

    if stack:                           # stak에 item, 즉 소괄호가 남아있다면 짝이 없는 괄호만 남아있는 것이기 때문에 'NO'를 출력한다.
        print("NO")
    else:
        print("YES")