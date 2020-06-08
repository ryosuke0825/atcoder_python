import sys
from collections import deque


def input():
    return sys.stdin.readline()[:-1]


H, W, N = map(int, input().split())
str_N = str(N)

sx, sy = 0, 0
M = [['X']*(W+2)]
for i in range(1, H+1):
    tmp = ''.join(['X', input(), 'X'])
    M.append(list(tmp))

    # 巣の位置
    if tmp.count('S') >= 1:
        sy = i
        sx = M[i].index('S')
M.append(['X']*(W+2))

# 移動できるのは東西南北（前後左右）
mv = [[1, 0], [-1, 0], [0, 1], [0, -1]]
next_cost = 1

# チーズの数だけ幅優先探索を繰り返す
for target in range(1, N+1):
    str_target = str(target)
    # 開始位置（最初は巣、次からは前回のチーズ工場の位置）
    q = deque([[sx, sy, next_cost-1]])
    checked = [[-1] * (W+2) for i in range(H+2)]

    # 幅優先探索でチーズを探す
    while True:
        x, y, cost = q.popleft()
        checked[y][x] = 1
        # 探しているチーズ工場の場合
        if M[y][x] == str_target:
            # 最後のチーズ工場なら終了
            if str_target == str_N:
                print(cost)
                exit(0)

            # 次の幅優先探索の初期値を記録して終了
            sx, sy, next_cost = x, y, cost+1
            break

        # 障害物以外且つ未探索なら座標を追加
        for i in range(len(mv)):
            tx = x+mv[i][0]
            ty = y+mv[i][1]
            if M[ty][tx] != 'X' and checked[ty][tx] == -1:
                q.append([tx, ty, cost+1])
                checked[ty][tx] = 1
