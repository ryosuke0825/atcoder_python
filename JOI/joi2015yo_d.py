# N日目に町Mにいる時の最小疲労度を求めていく
# dp[日付][町]

import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
D = [0]*(N+1)
for i in range(1, N+1):
    D[i] = int(input())

C = [0]*(M+1)
for i in range(1, M+1):
    C[i] = int(input())

INF = 10**18
dp = [[INF] * (N+1) for i in range(M+1)]

# 都市0にいる時の披露は必ず0である
for day in range(M+1):
    dp[day][0] = 0

for day in range(1, M+1):
    for town in range(1, N+1):
        # 今の値、待機する場合、1個前の町から移動する場合の最小を得る
        dp[day][town] = min(dp[day][town], dp[day-1][town], dp[day-1][town-1]+D[town]*C[day])
print(dp)

ans = INF
for i in range(M+1):
    if ans > dp[i][N]:
        ans = dp[i][N]
print(ans)
