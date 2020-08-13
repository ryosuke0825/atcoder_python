from collections import deque

# 建物以外のマスから建物があって進めない回数をカウントする

W, H = map(int, input().split())
M = [[0]*(W+2)]
for _ in range(H):
    tmp = list(map(int, input().split()))
    M.append([0]+tmp+[0])
M.append([0]*(W+2))

mv_even = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0)]
mv_odd = [(-1, 0), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

que = deque([])
que.append((0, 0))

check = [[-1] * (W+2) for i in range(H+2)]
check[0][0] = 0
ans = 0
while que:
    h, w = que.popleft()
    for mv_w, mv_h in (mv_even if h % 2 == 0 else mv_odd):
        nh = h+mv_h
        nw = w+mv_w

        if 0 <= nh < H+2 and 0 <= nw < W+2:
            if M[nh][nw] == 0 and check[nh][nw] == -1:
                # 建物がなくて、未訪問時
                check[nh][nw] = 0
                que.append((nh, nw))
            if M[nh][nw]:
                # 建物時は壁をカウントアップする
                ans += 1
print(ans)
