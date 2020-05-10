N, M, X = map(int, input().split())
CA = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    CA.append(tmp)

ans = -1
for i in range(2**N):
    tmp_cost = 0
    tmp_X = [0]*(M+1)
    for j in range(N):
        if ((i >> j) & 1):
            for k in range(M+1):
                tmp_X[k] += CA[j][k]
    for j in range(1, M+1):
        if tmp_X[j] < X:
            break
    else:
        if ans == -1:
            ans = tmp_X[0]
        else:
            ans = min(ans, tmp_X[0])
print(ans)
