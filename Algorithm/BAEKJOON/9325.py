# 얼마?

'''
s == 자동차 가격
n == 옵션 개수
q == 특정 옵션 개수
p == 해당 옵션 가격
'''

t =  int(input())
for _ in range(t):
    s = int(input())
    n = int(input())
    mutiply_qp = 0
    
    # if n == 0 :
    #     mutiply_qp == 0

    for i in range(n):
        q, p = map(int,input().split())

        mutiply_qp += (q * p)

    print(s + mutiply_qp)