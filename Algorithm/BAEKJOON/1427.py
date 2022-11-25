'''
소트인사이드
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

2143        => 4321
999998999   => 999999998
'''

N = map(int, input())
N = sorted(N, reverse=True)

print(''.join(map(str, N)))

