# 오븐 시계
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

'''
input = 14 30
        20

output = 14 50
'''

H, M = map(int, input().split())
cook = int(input())

hour = (M + cook) // 60
minute = (M + cook) % 60


if M + cook >= 60:
    M = (M + cook) - 60 

    if H + hour >= 24:
       H = H - 24
    H = H + hour
    print(H, minute)

else:
    if H >= 24:
       H = H - 24

    print(H, M + cook)