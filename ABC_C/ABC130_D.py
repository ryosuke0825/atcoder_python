N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
now_sum = 0
idx_r = 0
for idx_l in range(N):
    # K以上になるまで加算する
    while (idx_r < N) and (now_sum < K):
        now_sum += A[idx_r]
        idx_r += 1

    # 今の時点でK以上なので残りの要素数+1を加算する
    if now_sum >= K:
        ans += N-idx_r+1

    # 合計力から最も左の要素を減算する
    now_sum -= A[idx_l]

print(ans)
