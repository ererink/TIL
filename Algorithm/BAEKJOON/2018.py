N = int(input())

cnt = 1

for i in range(N + 1):
    sum = 0
    for j in range(i + 1, N + 1):
        if sum == N:
            cnt += 1
            break

        if sum > N:
            break

        sum += j

print(cnt)