import itertools

N, M, Q = map(int, input().split())
As = list(itertools.combinations_with_replacement(range(1, M + 1), N))

ans = [0]*len(As)
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    for i, A in enumerate(As):
        if A[b-1]-A[a-1] == c:
            ans[i] += d

print(max(ans))
