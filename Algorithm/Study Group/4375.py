# 백준 1
while True:
    try:
        n = int(input())
    except:
        break

    num = 0                     # 배수 찾기
    i = 1                       # 자리수 카운트

    while True:
        num = num * 10 + 1      # 1로 이루어진 배수를 찾는 것이므로 1을 더한다.
        if num % n == 0:        # 나머지가 0일 경우 배수
            print(i)
            break
        i += 1