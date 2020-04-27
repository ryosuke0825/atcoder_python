N, M = map(int, input().split())
XY = {}
for _ in range(M):
    x, y = input().split()
    XY[x+'_'+y] = True
    XY[y+'_'+x] = True

ans = 0
for i in range(2**N):
    kouho = []
    for j in range(N):
        if ((i >> j) & 1):
            kouho.append(j)

    # 候補が全員知り合いか
    for kijyun in kouho:
        for siriai in kouho:
            if kijyun == siriai:
                continue

            if not(str(kijyun+1)+'_'+str(siriai+1) in XY):
                break
        else:
            continue
        break
    else:
        ans = max(ans, len(kouho))

print(max(1, ans))
