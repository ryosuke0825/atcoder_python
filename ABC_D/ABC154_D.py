n, k = map(int, input().split())
pl = list(map(int, input().split()))

ave_pl = []
for i, p in enumerate(pl):
    p_sum = p*(p+1)/2
    if i == 0:
        ave_pl.append(p_sum/p)
    else:
        ave_pl.append(ave_pl[i-1]+(p_sum/p))

ans = 0
if n == k:
    print(ave_pl[-1])
else:
    for i in range(k-1, n):
        if i == 0:
            ans = max(ans, ave_pl[i])
        else:
            ans = max(ans, ave_pl[i]-ave_pl[i-k])
    print(ans)
