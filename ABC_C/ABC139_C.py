n = int(input())
H = list(map(int, input().split()))

ans = 0
cnt = 0
bh = H[0]
for i in range(1, n):
    if H[i] <= bh:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
    bh = H[i]
else:
    ans = max(ans, cnt)
print(ans)
