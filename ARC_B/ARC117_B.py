N = int(input())
A = list(map(int, input().split()))
MAD = 1000000007

A.sort()
ans = A[0]+1
ans %= MAD
for i in range(1, N):
    ans *= (A[i]-A[i-1]+1)
    ans %= MAD
print(ans)
