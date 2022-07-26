# 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

t = int(input())
for test_case in range(1, t + 1):
    
    n = int(input())
    cnt = 0
    for test_case_1 in range(0, n + 1):
        if test_case_1 % 2 == 1:
            cnt += test_case_1
        else:
            cnt -= test_case_1

    print('#{} {}'.format(test_case, cnt))