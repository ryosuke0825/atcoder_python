import sys
sys.setrecursionlimit(10 ** 6)


def input():
    return sys.stdin.readline()[:-1]


def dfs(now, prev=-1):
    for next in tree[now]:
        # 1個前のノードを参照した時はcontinue
        if next == prev:
            continue

        # 現在のポイントを次のノードへ加算して累積和をとる
        point[next] += point[now]

        # 次のノードへ
        dfs(next, now)


N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
point = [0]*N

# 木構造を2次元配列で表現。要素Xのノードからつながっているノード番号が格納される。
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

# 各ノードのポイントを求める
for _ in range(Q):
    p, x = map(int, input().split())
    point[p-1] += x

dfs(0)
print(*point)
