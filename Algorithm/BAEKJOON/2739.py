# 구구단

n = int(input())
result = 0

for i in range(1, 10):
    result += n * i
    print('{} * {} = {}'.format(n, i, result))
    result = 0