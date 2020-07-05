import sys


def input():
    return sys.stdin.readline()[:-1]


C = int(input())
flag = [[""] * 5 for i in range(C)]
for r in range(5):
    tmp = list(input())
    for c in range(C):
        flag[c][r] = tmp[c]

INF = 10**18
dp = [[INF] * (C+1) for i in range(3)]
for color in range(3):
    dp[color][0] = 0

COLOR_CODE = [('W', 0), ('B', 1), ('R', 2)]
for column in range(1, C+1):
    for color in COLOR_CODE:
        cost = 5-flag[column-1].count(color[0])
        if color[1] == 0:
            cost += min(dp[1][column-1], dp[2][column-1])
        elif color[1] == 1:
            cost += min(dp[0][column-1], dp[2][column-1])
        elif color[1] == 2:
            cost += min(dp[0][column-1], dp[1][column-1])
        dp[color[1]][column] = min(dp[color[1]][column], cost)

print(min(dp[0][-1], dp[1][-1], dp[2][-1]))
