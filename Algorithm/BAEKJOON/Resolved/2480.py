a, b, c = map(int, input().split())
dice = []

dice.append(a)
dice.append(b)
dice.append(c)


if a == b == c:
    print(10000 + a * 1000)
elif a == b and a != c:
    print(1000 + a * 100)

elif a == c and a != b:
    print(1000 + a * 100)

elif b == c and a != b:
    print(1000 + b * 100)

else:
    print(max(dice) * 100)
