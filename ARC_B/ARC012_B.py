N, va, vb, L = map(int, input().split())

for _ in range(N):
    s = L/va
    L = vb*s

    if L <= 0.000001:
        L = 0
        break
print(L)
