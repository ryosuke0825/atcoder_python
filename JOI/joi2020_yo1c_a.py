X, L, R = map(int, input().split())

ans = 0
if X <= L:
    ans = L
elif X >= R:
    ans = R
else:
    ans = X
print(ans)
