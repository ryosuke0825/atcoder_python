import numpy as np

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

S = np.array([[int(t == ".") for t in s] for s in S])

hw = []
for _ in range(H):
    tmp = list(input())
    hw.append(tmp)

L = []
for i in range(H):
    tmp = []
    if hw[i][0] == '.':
        tmp.append(1)
    else:
        tmp.append(0)

    for j in range(W-1):
        if hw[i][j+1] == '.':
            tmp.append(tmp[j]+1)
        else:
            tmp.append(0)
    L.append(tmp)

R = []
for i in range(H):
    tmp = [0]*W
    if hw[i][W-1] == '.':
        tmp[W-1] = 1
    else:
        tmp[W-1] = 0

    for j in reversed(range(W-1)):
        if hw[i][j] == '.':
            tmp[j] = tmp[j+1]+1
        else:
            tmp[j] = 0
    R.append(tmp)

U = [[0] * W for i in range(H)]
for i in range(W):
    if hw[0][i] == '.':
        U[0][i] = 1
    else:
        U[0][i] = 0

    for j in range(1, H):
        if hw[j][i] == '.':
            U[j][i] = U[j-1][i]+1
        else:
            U[j][i] = 0

D = [[0] * W for i in range(H)]
for i in range(W):
    if hw[H-1][i] == '.':
        D[H-1][i] = 1
    else:
        D[H-1][i] = 0

    for j in reversed(range(H-1)):
        if hw[j][i] == '.':
            D[j][i] = D[j+1][i]+1
        else:
            D[j][i] = 0

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)
print(ans)