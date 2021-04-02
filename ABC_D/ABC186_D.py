import itertools

N = int(input())
A = list(map(int, input().split()))

A.sort()
ac = list(itertools.accumulate(A))

ans = 0
for i in range(N):
    ans += A[i]*(i+1)-ac[i]
print(ans)
