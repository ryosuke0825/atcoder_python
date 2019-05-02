N, T = map(int, input().split())
ans = 1001
for i in range(N):
    tmp = list(map(int, input().split()))
    if tmp[1] <= T:
        ans = min(ans, tmp[0])

print(ans if ans != 1001 else "TLE")
