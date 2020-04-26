S = list(input())

ans = 0
for start_floor in range(len(S)):
    # 開始階のボタンが上の時
    if S[start_floor] == 'U':
        ans += (len(S)-1)-start_floor
        ans += start_floor*2

    # 開始階のボタンが下の時
    else:
        ans += ((len(S)-1)-start_floor)*2
        ans += start_floor
print(ans)
