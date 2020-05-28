import numpy as np
import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
H = [0]*N
S = [0]*N
for i in range(N):
    h, s = map(int, input().split())
    H[i] = h
    S[i] = s
H = np.array(H)
S = np.array(S)

# 最低点数と最高点数を設定する
ng = 0
ok = H.max()+N*S.max()
TB = np.arange(0, N)

# 成り立つ最低点数を二分探索で求める
while ng+1 < ok:
    m = (ng+ok)//2

    T = m-H
    T //= S
    T.sort()
    T -= TB
    if T.min() < 0:
        ng = m
    else:
        ok = m
print(ok)
