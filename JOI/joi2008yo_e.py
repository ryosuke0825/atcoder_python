import numpy as np

R, C = map(int, input().split())
moti = np.array([list(map(int, input().split())) for _ in range(R)])

ans = 0
for bit in range(1 << R):
    # numpyでは浅いコピーと深いコピーが自動判定される
    moti_c = moti.copy()

    for r in range(R):
        # 1の行はひっくり返す行
        if ((bit >> r) & 1):
            # 排他的論理和で値を反転させる
            moti_c[r] ^= 1

    # 各列の1の数をカウントする
    reverse_cnt = moti_c.sum(axis=0)

    # 各列を裏側の数を最大化した時の値を取得する
    column_max_cnt = np.maximum(reverse_cnt, R-reverse_cnt)

    ans = max(ans, column_max_cnt.sum())
print(ans)
