# 25304

'''
input = 
    260000  => 총 금액
    4       => 물건 종류의 수
    20000 5 => 가격 & 개수
    30000 2
    10000 6
    5000 8
'''

total = int(input())
n = int(input())
count_total= 0

for _ in range(n):
    price, m = map(int, input().split())
    count_total += (price * m)

if total == count_total:
    print('Yes')
else:
    print('No')