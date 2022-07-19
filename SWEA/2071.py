# 10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
# (소수점 첫째 자리에서 반올림한 정수를 출력한다.)

T = int(input())
for test_case in range(1, T + 1):

    nums = list(map(int, input().split()))
    avg = sum(nums) / len(nums)
    avg = round(avg)
    print('#{} {}'.format(test_case, avg))