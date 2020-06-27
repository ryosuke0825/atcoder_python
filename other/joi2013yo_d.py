import sys


def input():
    return sys.stdin.readline()[:-1]


D, N = map(int, input().split())

mx = [0]*D
for i in range(D):
    mx[i] = int(input())

abc = []*N
for i in range(N):
    abc.append(list(map(int, input().split())))

check = [[0] * N for i in range(D)]
for clothes in range(N):
    for day in range(D):
        if abc[clothes][0] <= mx[day] <= abc[clothes][1]:
            check[day][clothes] = 1

dp = [[0] * D for i in range(N)]
for day in range(1, D):
    for clothes1 in range(N):
        if check[day-1][clothes1] == 0:
            continue

        tmp_abs = 0
        tmp_clothes2 = 0
        for clothes2 in range(N):
            if check[day][clothes2] == 0:
                continue
            tmp_abs = abs(abc[clothes1][2]-abc[clothes2][2])

            dp[clothes2][day] = max(
                dp[clothes2][day], dp[clothes1][day-1]+tmp_abs)

ans = 0
for i in range(N):
    ans = max(ans, dp[i][-1])
print(ans)
