N, M = map(int, input().split())

ans = 0

# 最初からある「S」を使って作れるだけ「Scc」を作る
# 「c」の1/2より「S」の方が多い場合、作れるだけ「Scc」を作って終わり
if N > M/2:
    ans += M//2
    N -= M//2
    M = M % 2
    print(ans)
    exit(0)

# 「c」の方が多い時
# 「S」を使い切る
ans += N
M -= N*2
N = 0

# 残った「c」から作れるだけ「Scc」を作る
ans += M//4
print(ans)
