N = int(input())
W = list(map(int, input().split()))

ans = 10**9
for T in range(1, N+1):
    S1 = 0
    S2 = 0
    for i in range(0,len(W)):
        if (i <= T):
            S1 += W[i]
        else:
            S2 += W[i]
    ans = min(ans, abs(S1-S2))

print(ans)
