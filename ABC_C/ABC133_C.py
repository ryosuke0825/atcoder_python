L, R = map(int, input().split())

ans = 2018**2
if R-L >= 2019:
    ans = 0
else:
    l, r = L % 2019, R % 2019
    for i in range(l, r):
        for j in range(i+1, r+1):
            ans = min(ans, i*j % 2019)
print(ans)
