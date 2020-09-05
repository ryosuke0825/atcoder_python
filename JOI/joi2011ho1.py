import sys


def input():
    return sys.stdin.readline()[:-1]


M, N = map(int, input().split())
K = int(input())

S = []
for i in range(M):
    S.append(list(input()))

mj = [[0] * (N+1) for i in range(M+1)]
mo = [[0] * (N+1) for i in range(M+1)]
mi = [[0] * (N+1) for i in range(M+1)]

for y in range(1, M+1):
    j = 0
    o = 0
    i = 0
    for x in range(1, N+1):
        if S[y-1][x-1] == 'J':
            j += 1
        elif S[y-1][x-1] == 'O':
            o += 1
        elif S[y-1][x-1] == 'I':
            i += 1

        mj[y][x] += mj[y-1][x]+j
        mo[y][x] += mo[y-1][x]+o
        mi[y][x] += mi[y-1][x]+i

ans = [""]*K
for i in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    j = mj[y2][x2]-mj[y1-1][x2]-mj[y2][x1-1]+mj[y1-1][x1-1]
    o = mo[y2][x2]-mo[y1-1][x2]-mo[y2][x1-1]+mo[y1-1][x1-1]
    ice = mi[y2][x2]-mi[y1-1][x2]-mi[y2][x1-1]+mi[y1-1][x1-1]
    print(j, o, ice)
