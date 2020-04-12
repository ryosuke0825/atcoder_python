N = int(input())

TXY = []
for _ in range(N):
    txy = list(map(int, input().split()))
    TXY.append(txy)

t = 0
x = 0
y = 0
for i in range(N):
    # 必要な移動距離
    ido = abs(x-TXY[i][1])+abs(y-TXY[i][2])

    # 時間までにたどり着けるか
    if ido > TXY[i][0]-t:
        break

    # その場所にいることができるか
    if ido % 2 != (TXY[i][0]-t) % 2:
        break

    t = TXY[i][0]
    x = TXY[i][1]
    y = TXY[i][2]

else:
    print('Yes')
    exit(0)
print('No')
