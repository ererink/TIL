import sys

t = int(input())
for test_case in range(1, t + 1):

    submit_stu = []
    no_submit = []

    n, k = map(int, input().split())
    submit_stu = list(map(int, input().split()))

    for i in range(1, n + 1) :
        if i not in submit_stu :
            no_submit.append(i)

    print(f'#{test_case}', *no_submit)