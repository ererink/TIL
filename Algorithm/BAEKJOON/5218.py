t = int(input())
for _ in range(t):
    w1, w2 = input().split()
    check = []

    for i in range(len(w1)):
        if ord(w1[i]) > ord(w2[i]):
            check.append(26 - (ord(w1[i]) - ord(w2[i])))
        else:
            check.append(ord(w2[i]) - ord(w1[i]))

    print("Distances:", *check)