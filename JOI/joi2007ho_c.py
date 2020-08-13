n = int(input())

xyl = []
for _ in range(n):
    xy = tuple(map(int, input().split()))
    xyl.append(xy)

xy_set = set(xyl)
ans = 0
for i in range(n):
    # 1つ目の柱の座標
    x1, y1 = xyl[i]

    for j in range(i+1, n):
        # 2つ目の柱の座標
        x2, y2 = xyl[j]

        # 3つ目の柱の座標
        x3 = x2-y2+y1
        y3 = y2+x2-x1

        # 4つ目の柱の座標
        x4 = x1-y2+y1
        y4 = y1+x2-x1

        if (x3, y3) in xy_set and (x4, y4) in xy_set:
            ans = max(ans, (x1-x2)**2+(y1-y2)**2)

print(ans)
