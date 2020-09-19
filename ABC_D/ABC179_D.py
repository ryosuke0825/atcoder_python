N, K = map(int, input().split())
MOD = 998244353

lr = []
for _ in range(K):
    l, r = map(int, input().split())
    lr.append((l, r))
lr.sort()

dp = [0]*(N+1)
dpsum = [0]*(N+1)
dp[1] = 1
dpsum[1] = 1
for i in range(2, N+1):
    for l, r in lr:
        lj = max(1, i-r)
        rj = i-l

        if rj < 1:
            continue

        dp[i] += dpsum[rj]-dpsum[lj-1]
        dp[i] %= MOD
    dpsum[i] = dp[i]+dpsum[i-1]

print(dp[N])
