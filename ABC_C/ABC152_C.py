import itertools

N = int(input())
P = list(map(int, input().split()))

a = list(itertools.accumulate(P, func=min))
ans = 0
for i in range(N):
    if P[i] <= a[i]:
        ans += 1

print(ans)
