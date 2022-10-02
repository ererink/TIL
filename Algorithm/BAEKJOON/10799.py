# 쇠막대기
# 스택 & 큐

'''
input = ()(((()())(())()))(())
'''

# (은 스택에 넣어준다. 
# )가 나오면 스택에서 (를 빼준다. 
# (를 빼줄 때 스택의 (의 개수만큼 카운트한다. 

steel_bar = list(input())
cnt = 0
stack = []

for i in range(len(steel_bar)):
    if steel_bar[i] == '(':
        stack.append(steel_bar[i])
    
    else:
        if steel_bar[i - 1] == '(':
            stack.pop()
            cnt += len(stack)
        
        else:
            stack.pop()
            cnt += 1
    

print(cnt)

