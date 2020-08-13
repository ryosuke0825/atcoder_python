N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 21 for i in range(N-1)]
dp[0][A[0]] = 1

for i in range(1, N-1):
    a = A[i]
    for j in range(0, 21):
        if j+a <= 20 and dp[i-1][j] >= 1:
            dp[i][a+j] += dp[i-1][j]
        if j-a >= 0 and dp[i-1][j] >= 1:
            dp[i][j-a] += dp[i-1][j]
print(dp[-1][A[-1]])
