N = int(input())
A = list(map(int, input().split()))

if A.count(0) >= 1:
    print(0)
    exit(0)

L = 10**18
ans = A[0]
for i in range(1, N):
    ans *= A[i]
    if ans > L:
        print(-1)
        exit(0)
print(ans)
