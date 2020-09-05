S = input()

# 25の繰り返し回数毎に出現回数をカウントする
cnt = {}
tmp_cnt = 0
flg = False
cnt_max = 0
for i in range(0, len(S)-1):
    if flg:
        flg = False
        continue
    if S[i] == '2' and S[i+1] == '5':
        tmp_cnt += 1
        flg = True
    elif tmp_cnt > 0:
        if tmp_cnt in cnt:
            cnt[tmp_cnt] += 1
        else:
            cnt[tmp_cnt] = 1
            if tmp_cnt > cnt_max:
                cnt_max = tmp_cnt
        tmp_cnt = 0
if tmp_cnt > 0:
    if tmp_cnt in cnt:
        cnt[tmp_cnt] += 1
    else:
        cnt[tmp_cnt] = 1

ans = 0
tmp = 0
for i in cnt.keys():
    ans += (i*(i+1)//2)*cnt[i]
print(ans)
