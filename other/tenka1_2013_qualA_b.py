N = int(input())
ans = 0
for _ in range(N):
    vwxyz = list(map(int, input().split()))
    if sum(vwxyz) < 20:
        ans += 1
print(ans)
