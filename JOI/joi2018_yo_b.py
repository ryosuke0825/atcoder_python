N = int(input())
A = list(map(int, input().split()))

ans = 0
tmp = 0
for i in range(N):
    if A[i] == 1:
        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 0
ans = max(ans, tmp)

print(ans+1)
