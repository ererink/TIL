# 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.

# (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)

t = int(input())
for test_case in range(1, t + 1):


    h1, m1, h2, m2 = map(int, input().split())
    result1 = h1 + h2            
    result2 = m1 + m2
    if result1 > 12:
            result1 -=  12
    if result2 > 59:
            result1 += 1
            result2 -= 60

    print('#{} {} {}'.format(test_case, result1, result2))