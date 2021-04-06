N, M, Q = map(int, input().split())

# 隣接リスト
tree = [[] for i in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    tree[u-1].append(v-1)
    tree[v-1].append(u-1)

# 拡張点の初期色
color = list(map(int, input().split()))

for _ in range(Q):
    q = list(map(int, input().split()))
    q[1] -= 1

    # クエリの種類毎に分岐する
    if q[0] == 1:
        # スプリンクラー起動
        print(color[q[1]])
        for n in tree[q[1]]:
            color[n] = color[q[1]]
    else:
        # 対象の頂点の色を上書き
        print(color[q[1]])
        color[q[1]] = q[2]
