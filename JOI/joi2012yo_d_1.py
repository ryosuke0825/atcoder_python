# 制約なし

N, K = map(int, input().split())

# N日間*3種類の配列を用意する。
dp = [[0] * 3 for _ in range(N)]

# 1日目
day = 0
dp[day] = [1] * 3

# 2日目～N日目
for day in range(1, N):
    for pasta in range(3):
        dp[day][pasta] = sum(dp[day-1])
print(sum(dp[-1]))
