# 주어진 숫자부터 0까지 순서대로 찍어보세요.
# 입력된 숫자가 N일 때 거꾸로 출력한다. 

n = int(input())
for i in range(n, -1, -1) :
    print(i, end=' ')