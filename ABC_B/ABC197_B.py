H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1

S = []
for _ in range(H):
    s = list(input())
    S.append(s)

# 自身に障害物があるか
if S[X][Y] == '#':
    print(0)
    exit(0)

ans = 1

# 上を見る
if X != 0:
    for h in range(X-1, -1, -1):
        if S[h][Y] == '.':
            ans += 1
        else:
            break

# 下を見る
if X != H-1:
    for h in range(X+1, H):
        if S[h][Y] == '.':
            ans += 1
        else:
            break

# 右を見る
if Y != W-1:
    for w in range(Y+1, W):
        if S[X][w] == '.':
            ans += 1
        else:
            break

# 左を見る
if Y != 0:
    for w in range(Y-1, -1, -1):
        if S[X][w] == '.':
            ans += 1
        else:
            break

print(ans)
