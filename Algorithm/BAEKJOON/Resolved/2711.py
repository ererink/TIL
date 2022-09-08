t = int(input())
for _ in range(t):
    result = ''    
    n, w = input().split()
    
    for i in range(len(w)):
        if i == int(n) - 1:
            continue
        else:
            result += w[i]

    print(result)


