H, W = map(int, input().split())
A = []
mi = 100
for _ in range(H):
    a = list(map(int, input().split()))
    mi = min(min(a), mi)
    A.append(a)

ans = 0
for h in range(H):
    for w in range(W):
        ans += A[h][w]-mi
print(ans)
