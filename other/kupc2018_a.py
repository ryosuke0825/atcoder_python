N = int(input())
S = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans = max(ans, S[i]*A[i])

print(ans)
