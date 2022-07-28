# 서랍의 비밀번호

P, K = map(int, input().split())
cnt = 0
for i in range(K, P + 1):
    cnt += 1
    
print(cnt)