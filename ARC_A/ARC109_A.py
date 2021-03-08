A, B, X, Y = map(int, input().split())

ans = 0
if A == B:
    # 同じ階
    ans = X
elif A > B:
    # 建物Bの1個下の階へ斜め移動して、下階段
    ans1 = X+((abs(A-B)-1)*Y)
    # 建物Bの1個下の階へ斜め移動してA塔へ戻るの繰り返し
    ans2 = abs(A - B)*X*2-X
    ans = min(ans1, ans2)
else:
    # 建物Bへ横移動して、上階段
    ans1 = X+(abs(A - B)*Y)
    # 建物Bへ横移動して斜め上で建物Aへ戻るの繰り返し
    ans2 = abs(A - B)*X*2+X
    ans = min(ans1, ans2)
print(ans)
