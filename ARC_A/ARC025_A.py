D = list(map(int, input().split()))
J = list(map(int, input().split()))

ans = 0
for i in range(len(D)):
    ans += max(D[i], J[i])
print(ans)
