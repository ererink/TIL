# 빨강(red), 초록(green), 파랑(blue) 빛을 섞어 여러 가지 다른 색 빛을 만들어 내려고 한다.

# 빨강(r), 초록(g), 파랑(b) 각 빛의 가짓수가 주어질 때,
# 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합(r g b)과 만들 수 있는 색의 가짓 수를 계산해보자.  

r, g, b = map(int, input().split())

cnt = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print('%d %d %d' %(i, j, k))

            cnt += 1

print(cnt)
