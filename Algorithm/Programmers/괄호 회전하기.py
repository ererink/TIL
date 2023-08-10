from collections import deque
def solution(s):
    answer = 0
    n = len(s)
    s = deque(s)
    
    # 올바른 괄호 검사
    def check():
        nonlocal s
        nonlocal answer
        chk = []
        flag = 0 # 올바른 괄호 발견

        for j in range(n):
            if s[j] == ')':
                if chk:
                    if '(' == chk[-1]:
                        chk.pop()
                        flag = 1
                    else:
                        flag = 0
                        break
                
            elif s[j] == ']':
                if chk:
                    if '[' == chk[-1]:
                        chk.pop()
                        flag = 1
                    else:
                        flag = 0
                        break
                
            elif s[j] == '}':
                if chk:
                    if '{' == chk[-1]:
                        chk.pop()
                        flag = 1
                    else:
                        flag = 0
                        break
                
            else:
                 chk.append(s[j])

        if flag == 1 and not chk:
            answer += 1
            
    # 회전
    for i in range(n):
        if i != 0:
            s.append(s.popleft())
        check()
            
    return answer