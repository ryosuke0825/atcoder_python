import sys
import bisect


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())

# 1投目だけの場合に対応するために、N+1のリストを作成している
P = [0]*(N+1)
for i in range(N):
    P[i] = int(input())

# 1投目と2投目の全ての合計点を作成する
one_two = sorted([a+b for i, a in enumerate(P) for b in P[i:]])

one_two.sort()
ans = 0
for i in range(len(one_two)):
    if one_two[i] < M:
        ans = max(ans, one_two[i])

    # 残り何点まで取得できるか
    x = M-one_two[i]
    if x > 0:
        idx = bisect.bisect_left(one_two, x)
        if idx > 0 and one_two[i]+one_two[idx-1] < M:
            ans = max(ans, one_two[i]+one_two[idx-1])
print(ans)
