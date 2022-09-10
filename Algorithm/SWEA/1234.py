for test_case in range(1, 11):
    a, nums = input().split()
    nums = list(nums)
    stack = []
    answer = ''

    for i in nums:
        if len(stack) > 0:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        
        else:
            stack.append(i)

    for j in stack:
        answer += j

    print('#{} {}'.format(test_case, answer))