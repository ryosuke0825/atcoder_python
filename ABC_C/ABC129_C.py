N, M = map(int, input().split())
A = {}
for _ in range(M):
    a = int(input())
    A[a] = True

dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

for i in range(2, N+1):
    # 壊れた床がなく単純に求める場合
    #dp[i] = dp[i-1]+dp[i-2]

    if not i-1 in A:
        dp[i] += dp[i-1]
    if not i-2 in A:
        dp[i] += dp[i-2]

print(dp[N] % 1000000007)
