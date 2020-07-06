N, X = map(int, input().split())
A = list(map(int, input().split()))

a_max = max(A)
ans = 0
for a in A:
    if a+X >= a_max:
        ans += 1
print(ans)
