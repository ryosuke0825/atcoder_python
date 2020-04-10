H, W = map(int, input().split())

S = []
for _ in range(H):
    tmp = list(input())
    S.append(tmp)

for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            # 上
            if h > 0 and S[h-1][w] == '#':
                continue
            # 下
            elif h < H-1 and S[h+1][w] == '#':
                continue
            # 左
            elif w > 0 and S[h][w-1] == '#':
                continue
            # 右
            elif w < W-1 and S[h][w+1] == '#':
                continue
            print('No')
            exit(0)

print('Yes')

