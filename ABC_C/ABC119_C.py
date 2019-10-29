# N本の竹、必要な3本の竹の長さはABC
N, A, B, C = map(int, input().split())
# 現在持っているそれぞれの竹の長さ（最大8本）
l = [int(input()) for i in range(N)]
INF = 10**9


def dfs(cur, a, b, c):
    # 竹の本数が全ての竹の場合だけ求める
    if cur == N:
        # min(a, b, c) > 0 は最低でも竹を作るには1本以上の竹が必要なため
        if min(a, b, c) > 0:
            # 現在（合体後）のabcそれぞれの竹の長さからABCにするの必要なコストを求める
            # 最初の再帰呼び出し時は合体をしていないので10*ABC3種分の30は引く
            return abs(a-A)+abs(b-B)+abs(c-C)-30
        else:
            return INF

    # 4のn乗の全探索をする
    ret0 = dfs(cur + 1, a, b, c)
    # 竹の追加＝合体なので+10している
    ret1 = dfs(cur + 1, a + l[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + l[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + l[cur]) + 10
    return min(ret0, ret1, ret2, ret3)


print(dfs(0, 0, 0, 0))
