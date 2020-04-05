n, m, Q = map(int, input().split())

# 二次元累積和の表を作る
M = [[0]*n for _ in range(n)]

# 列車の区間に該当するマスを+1する
for i in range(m):
    l, r = map(int, input().split())
    M[r-1][l-1] += 1
for i in reversed(range(n)):
    print(M[i])
print('============================')

# 各行で右から左へ累積和する
for q in range(n):
    for p in reversed(range(1, n)):
        M[q][p-1] += M[q][p]
for i in reversed(range(n)):
    print(M[i])
print('============================')

# 各列で下から上へ累積和する
for p in range(n):
    for q in range(n-1):
        M[q+1][p] += M[q][p]
for i in reversed(range(n)):
    print(M[i])
print('============================')

# クエリの値を求める
for i in range(Q):
    p, q = map(int, input().split())
    print(M[q-1][p-1])
