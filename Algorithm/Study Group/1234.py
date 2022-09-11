for test_case in range(1, 11):
    a, nums = input().split()
    nums = list(nums)
    stack = []                                      # 같은 번호가 아닌 입력값이 들어간다.
    answer = ''

    for i in nums:
        if len(stack) > 0:                          # 스택에 값이 있는 경우
            
            if i == stack[-1]:                      # 입력값이 스택의 마지막 값과 같다면
                stack.pop()                         # 스택의 값을 제거한다. 
            
            else:
                stack.append(i)                     # 아니라면 스택에 입력값을 넣어준다.
        
        else:
            stack.append(i)                         # 스택에 값이 없다면 입력값을 넣어준다. 

    for j in stack:                                 # 입력값을 넣은 스택을 반복문을 통해 answer 변수에 넣어준다.
        answer += j

    print('#{} {}'.format(test_case, answer))