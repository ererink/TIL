# 오타맨 고창영

t = int(input())
for _ in range(t):
    n, w = input().split()
    answer = ''
    
    for i in range(len(w)):
        if i == int(n) -1:
            continue

        answer += w[i]

    print(answer)