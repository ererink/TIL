#피보나치 수

dp = [0] * 46
dp[1] = 1

for i in range(2, 46):
    dp[i] = dp[i - 2] + dp[i - 1]

n = int(input())
print(dp[n])