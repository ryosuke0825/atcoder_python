n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(n):
    if A[i] >= B[i]:
        ans += B[i]
        A[i] -= B[i]
    else:
        ans += A[i]
        B[i] -= A[i]
        ans += min(A[i+1], B[i])
        A[i+1] = max(0, A[i+1]-B[i])

print(ans)
