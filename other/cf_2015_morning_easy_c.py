N, K, M, R = map(int, input().split())

S = []
for _ in range(N-1):
    S.append(int(input()))

S.sort(reverse=True)

if sum(S[:K])/K >= R:
    print(0)
else:
    if R*K-sum(S[:K-1]) > M:
        print(-1)
    else:
        print(R*K-sum(S[:K-1]))
