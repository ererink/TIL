# 주사위 세개

# 내 제출
dices = list(map(int, input().split()))


for i in dices :
    if dices.count(i) == 3:
        print(10000 + i * 1000)
        break
    

    elif dices.count(i) == 2:
        print(1000 + i * 100)
        break

    else:
        print(max(dices) * 100)
        break

# 답안
a , b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)

elif a == b:
    print(1000 + a * 100)

elif a == c:
    print(1000 + a * 100)

elif b == c:
    print(1000 + b * 100)

else:
    print(max(a, b, c) * 100)