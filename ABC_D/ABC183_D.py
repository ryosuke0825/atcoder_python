N, W = map(int, input().split())

imos = [0]*((10**5)*2+1)
for _ in range(N):
    S, T, P = map(int, input().split())
    imos[S] += P
    imos[T] -= P

mx = imos[0]
for i in range(1, (10**5)*2+1):
    imos[i] += imos[i-1]
    mx = max(mx, imos[i])

if mx <= W:
    print('Yes')
else:
    print('No')
