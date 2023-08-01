from collections import deque
def solution(s):
    answer = True
    
    chk = deque()
    for i in s:
        # 맨 처음 괄호가 ')'일 경우
        if i == ')':
            if not chk:
                return False
        if i == ')':
            if '(' in chk:
                chk.popleft()
        else:
            chk.append(i)
    
    if chk:
        return False
    else:
        return True

    