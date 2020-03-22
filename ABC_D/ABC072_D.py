n = int(input())
P = list(map(int, input().split()))

ans = 0
for i in range(n):
    if i == n-1 and P[i] == i+1:
        ans += 1
    elif P[i] == i+1:
        P[i], P[i+1] = P[i+1], P[i]
        ans += 1
print(ans)
