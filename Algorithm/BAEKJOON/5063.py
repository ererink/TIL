# TGN

'''
r = 광고 X
e = 광고 O
c = 광고비
'''

N = int(input())
for test_case in range(N):

    r, e, c = map(int, input().split())
    if r > e - c:
        print('do not advertise')

    if r == e - c:
        print('does not matter')

    if r < e - c:
        print('advertise')