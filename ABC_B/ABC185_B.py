N, M, T = map(int, input().split())
AB = [list(map(int, input().split())) for i in range(M)]

now_time = 0
battery = N

ans = 'Yes'
for a, b in AB:

    # カフェに付くまでにの消費
    battery -= a-now_time
    if battery <= 0:
        ans = 'No'
        break

    # カフェでの充電
    battery += b-a
    battery = min(battery, N)

    # 現在時刻をカフェを出る時間に更新
    now_time = b

# 最後のカフェを出てから帰宅までの消費
battery -= T-now_time
if battery <= 0:
    ans = 'No'
print(ans)
