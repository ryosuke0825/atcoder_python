N = int(input())

AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append([a, b])

ans = -1
for i in range(N):
    for j in range(N):
        tmp = 0
        for k in range(N):
            # 入り口からマスAの商品までの移動距離
            tmp += abs(AB[i][0]-AB[k][0])

            # マスAからマスBの商品までの移動距離
            tmp += abs(AB[k][0]-AB[k][1])

            # マスBの商品から出口までの移動距離
            tmp += abs(AB[k][1]-AB[j][1])
        if ans == -1:
            ans = tmp
        else:
            ans = min(ans, tmp)
print(ans)
