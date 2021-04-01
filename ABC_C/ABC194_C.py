N = int(input())
A = list(map(int, input().split()))

# 要素の個数を数える。負の数があるので＋200している
mx = 200
cnt = [0 for i in range(401)]
for a in A:
    cnt[a+mx] += 1

# 差のパターンは400*400=16,000パターンなので全て試す。
# 存在しないパターンはcnt[i]、cnt[j]のどちらかが0なので0が加算されるのでOK。
ans = 0
for i in range(401):
    for j in range(i+1, 401):
        ans += cnt[i]*cnt[j]*(j-i)**2
print(ans)
