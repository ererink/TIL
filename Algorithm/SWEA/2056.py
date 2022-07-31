# 연월일 달력

t = int(input())
for test_case in range(1, t + 1) :
    date = input()

result = date[:4] + '/' + date[4:] 

print('#{} {}'.format(test_case, result))