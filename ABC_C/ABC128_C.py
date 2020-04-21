switch, light = map(int, input().split())
K = []
for _ in range(light):
    k = list(map(int, input().split()))
    K.append(k)
P = list(map(int, input().split()))

ans = 0
# bit全探索で全パターンをチェックする
for i in range(2**switch):

    # 各電球につながっているスイッチが何個ONか
    switch_on_list = [0]*light

    # 各スイッチの状態チェック
    for j in range(switch):
        # スイッチが付いているか
        if ((i >> j) & 1):
            # スイッチがつながっているライトを+1
            for k in range(light):
                for l in range(1, K[k][0]+1):
                    if j == K[k][l]-1:
                        switch_on_list[k] += 1

    # 電球が点灯する数のスイッチがONか
    for j in range(light):
        if switch_on_list[j] % 2 != P[j]:
            break
    else:
        ans += 1

print(ans)
