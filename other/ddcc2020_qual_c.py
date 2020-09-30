H, W, K = map(int, input().split())
S = []
for _ in range(H):
    tmp = list(input())
    S.append(tmp)

ans = [[0] * W for i in range(H)]
check = [[0] * W for i in range(H)]
cnt = 0
for h in range(H):
    for w in range(W):
        if S[h][w] == '.':
            continue

        cnt += 1
        ans[h][w] = cnt
        check[h][w] = cnt

        # 別の苺があるまで左に進む
        left = w
        if w != 0:
            for i in range(w-1, -1, -1):
                if S[h][i] == '#' or ans[h][i] != 0:
                    break
                ans[h][i] = cnt
                check[h][i] = cnt
                left -= 1

        # 別の苺があるまで右に進む
        right = w
        if w != W-1:
            for i in range(w+1, W):
                if S[h][i] == '#' or ans[h][i] != 0:
                    break
                ans[h][i] = cnt
                check[h][i] = cnt
                right += 1

        # 左右の幅だけ上側に苺がなくて切られていないなら切る範囲にする
        if h != 0:
            for i in range(h-1, -1, -1):
                flg = False
                for j in range(left, right+1):
                    if S[i][j] == '#' or check[i][j] != 0:
                        flg = True
                        break
                else:
                    for j in range(left, right+1):
                        ans[i][j] = cnt
                        check[i][j] = cnt
                if flg:
                    break

        # 左右の幅だけ下側に苺がなくて切られていないなら切る範囲にする
        if h != H-1:
            for i in range(h+1, H):
                flg = False
                for j in range(left, right+1):
                    if S[i][j] == '#' or check[i][j] != 0:
                        flg = True
                        break
                else:
                    for j in range(left, right+1):
                        ans[i][j] = cnt
                        check[i][j] = cnt
                if flg:
                    break
for i in range(H):
    print(' '.join(map(str, ans[i])))
