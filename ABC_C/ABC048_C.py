N, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, len(a)):
    # 2組の合計がxよりも大きいなら
    if a[i-1] + a[i] > x:
        # 右側の数が0より大きいなら食べる
        if a[i] > 0:
            # 右側の箱の飴をすべて食べてもx以上ならすべて食べる
            if (a[i-1] + a[i] - x) > a[i]:
                ans += a[i]
                a[i] = 0
            # 右側の箱の飴を食べるだけでx以下になるならその分だけ食べる
            else:
                ans += (a[i-1] + a[i] - x)
                a[i] = a[i] - (a[i-1] + a[i] - x)

        # 右の箱を食べただけでx以下にならない時は左側の箱の飴も食べる
        if a[i-1] + a[i] > x:
            # x以下になるために必要な分だけ飴を食べる
            ans += (a[i-1] + a[i] - x)
            a[i-1] = a[i-1] - (a[i-1] + a[i] - x)

print(ans)
