import collections

S = int(input())

ans = 'No'
if S < 10:
    # 1桁の場合
    if S == 8:
        ans = 'Yes'
elif S < 100:
    # 2桁の場合
    if S % 8 == 0:
        ans = 'Yes'
    else:
        rs = int(str(S)[1]+str(S)[0])
        if rs % 8 == 0:
            ans = 'Yes'
else:
    # 3桁以上の場合
    # 下3桁が8の倍数なら8の倍数になる

    # Sに各数値が何個あるかhashを作る
    s_dic = collections.Counter(list(str(S)))

    # 3桁の8の倍数（104～992）以下の8の倍数を作れるか全て試す
    for hachi in range(104, 1000, 8):
        hachi_dic = collections.Counter(list(str(hachi)))
        # Sにhachiを構成する全ての値があるなら8の倍数である（入力値に0は含まれない）
        for k in hachi_dic.keys():
            if hachi_dic[k] > s_dic[k]:
                break
        else:
            ans = 'Yes'

print(ans)
