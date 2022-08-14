n = int(input())
cal_n = n
cnt = 0

while True:
    a = cal_n // 10
    b = cal_n % 10
    c = (a + b) % 10
    cal_n = (b * 10) + c

    cnt += 1

    if cal_n == n:
        break

print(cnt)

