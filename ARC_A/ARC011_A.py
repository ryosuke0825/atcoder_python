m, n, N = map(int, input().split())

ans = 0
small_pen = 0
while True:
    # 使い切る
    ans += N
    small_pen += N
    N = 0

    # これ以上再生できない
    if small_pen < m:
        print(ans)
        exit(0)

    # 再生する
    N = (small_pen//m)*n
    small_pen %= m
