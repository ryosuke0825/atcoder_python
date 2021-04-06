N = int(input())

left = 0
right = N+1

# N+1の丸太で作れる最大の丸太数を二分探索で求める
while right-left > 1:
    # 作れる丸太の本数を等差数列の和の公式で求める
    x = (right + left) // 2
    wa = x*(x+1)//2
    if wa <= N+1:
        # 作れる本数の場合
        left = x
    else:
        # 作れない本数の場合
        right = x
print(N+1-left)
