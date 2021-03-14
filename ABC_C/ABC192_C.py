N, K = map(int, input().split())

ans = N
for _ in range(K):
    g1 = int("".join(sorted(str(ans), reverse=True)))
    g2 = int("".join(sorted(str(ans))))
    ans = g1-g2
print(ans)
