N = int(input())
T = []
for _ in range(N):
    t = int(input())
    T.append(t)

ans = 201
for i in range(2**N):
    A = 0
    B = 0
    for j in range(N):
        if ((i >> j) & 1):
            A += T[j]
        else:
            B += T[j]
    ans = min(ans, max(A, B))
print(ans)
