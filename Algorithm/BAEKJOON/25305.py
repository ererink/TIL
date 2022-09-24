n, k = map(int, input().split())
score = list(map(int,input().split()))

score = sorted(score, reverse=True)

print(score[k-1])