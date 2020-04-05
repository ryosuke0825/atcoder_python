N, K = map(int, input().split())

N = N % K
ans1 = abs(N - K)
ans2 = abs(ans1-K)
print(min(ans1, ans2))
