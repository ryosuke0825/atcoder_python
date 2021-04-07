N = int(input())
A = list(map(int, input().split()))

# 全ての区間を全探索する
ans = 0
for left in range(N):
    x = A[left]
    for right in range(left, N):
        # 左端を固定して最小値を更新していくのでminが不要になる
        x = min(x, A[right])
        # 皿の数＝右端-左端+1
        ans = max(ans, (right-left+1)*x)
print(ans)
