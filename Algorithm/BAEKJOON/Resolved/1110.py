N = int(input())
d = N
cnt = 0

while True:
    a = d // 10
    b = d % 10
    c = (a + b) % 10 # 2 + 6 = 8
    d = (b * 10) + c # 88 = 80 + 8 
    cnt += 1


    if d == N:
        break

print(cnt)
