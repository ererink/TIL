'''
n = 사람 수
m = 붕어빵을 만드는 시간
k = 붕어빵 개수
a, b = 손님이 도착하는 시간
'''

for test_case in range(int(input())):
    n, m, k = map(int, input().split())
    a = map(int, input().split())

    # if m <= a:
    #     if 