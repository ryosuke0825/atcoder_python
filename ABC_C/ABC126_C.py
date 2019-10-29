N, K = map(int, input().split())

ans = 0
for i in reversed(range(1, N+1)):
    n = 1
    # i番目のサイコロの目（=i）がKを超えるには何回コインで面を出す必要があるか
    while i < K:
        # 2倍にしている
        n = n*2
        i = i*2
    # Kを超える確率（=超えるために必要なコインが連続で表になる確率をansに加算する）
    ans += 1/n

# ansには各目が出る確率の合計が格納されているので値をN（サイコロの目の数）で割る
print(ans/N)
