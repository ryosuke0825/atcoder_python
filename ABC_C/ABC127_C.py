n, m = map(int, input().split())

ans_l = 0
ans_r = n
for _ in range(m):
    l, r = map(int, input().split())
    ans_l = max(ans_l, l)
    ans_r = min(ans_r, r)
print(max(0,ans_r-ans_l+1))
