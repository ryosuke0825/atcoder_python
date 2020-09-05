N, K = map(int, input().split())

# 食べるパスタの種類が決まっている日の入力。
reservation = {}
for _ in range(K):
    a, b = map(int, input().split())
    reservation[a-1] = (b-1)

# N日間*3種類の配列を用意する。
dp = [[0] * 3 for _ in range(N)]

# 1日目、とりあえず1にして予約されていたら予約外のパスタは0にする。
day = 0
dp[day] = [1] * 3
if day in reservation:
    for pasts in range(3):
        if pasts != reservation[day]:
            dp[day][pasts] = 0

# 2日目、
# 予約あり、対象のパスタに1日目の3種の値の合計値を入れる。
# 予約なし、全てのパスタに1日目の3種の値の合計値を入れる。
day = 1
for pasta in range(3):
    if day in reservation:
        if reservation[day] == pasta:
            dp[day][pasta] += sum(dp[day-1])
    else:
        dp[day][pasta] = sum(dp[day-1])

# 3日目～N日目
for day in range(2, N):
    for pasta in range(3):
        # 当日は予約されていない 又は 予約されている且つ予約されたパスタの場合
        if not(day in reservation) or (day in reservation and pasta == reservation[day]):
            # 前日に対象のパスタを食べている（=3日連続制約を考慮する必要がある）
            if dp[day-1][pasta] != 0:
                # 前日と2日前の3種の合計値から、前日と2日前の対象のパスタの合計値（3日連続した組み合わせ）を減算した値
                # 3日連続していない場合は値が0なので問題ない。
                dp[day][pasta] = sum(dp[day-1])+sum(dp[day-2])-(dp[day-1][pasta]+dp[day-2][pasta])
            else:
                # 前日に食べていない場合は3種の合計値（=3日連続制約を考慮しない）
                dp[day][pasta] = sum(dp[day-1])

print(sum(dp[-1]) % 10000)
