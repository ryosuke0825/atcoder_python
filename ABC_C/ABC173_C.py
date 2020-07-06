import copy

H, W, K = map(int, input().split())

hw = []
for _ in range(H):
    tmp = list(input())
    hw.append(tmp)

ans = 0
for hi in range(2**H):
    tmp_hw = copy.deepcopy(hw)
    for hj in range(H):
        if ((hi >> hj) & 1):
            # bitが立っている時の操作
            for i in range(W):
                tmp_hw[hj][i] = 'x'

    tmp_cnt = 0
    for i in range(H):
        tmp_cnt += tmp_hw[i].count('#')
    if tmp_cnt < K:
        continue

    for wi in range(2**W):
        tmp_hw2 = copy.deepcopy(tmp_hw)
        for wj in range(W):
            if ((wi >> wj) & 1):
                # bitが立っている時の操作
                for i in range(H):
                    tmp_hw2[i][wj] = 'x'
        cnt = 0
        for i in range(H):
            cnt += tmp_hw2[i].count('#')
        if cnt == K:
            ans += 1
print(ans)
