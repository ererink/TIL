# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램을 작성하라.

T = int(input())
for test_case in range(1, T + 1):

    a, b = map(int, input().split())
    if a < b:
        print('#{} {}'.format(test_case, '<'))
    elif a > b:
        print('#{} {}'.format(test_case, '>'))
    else:
        print('#{} {}'.format(test_case, '='))
