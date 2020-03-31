n = int(input())
A = list(map(int, input().split()))

A_cumsum = [0]
for i in range(n):
    A_cumsum.append(A_cumsum[i]+A[i])

for i in range(1, n+1):
    ans = 0
    for j in range(i, n+1):
        ans = max(ans, A_cumsum[j]-A_cumsum[j-i])
    print(ans)
