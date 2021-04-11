# 2人の異なる回答がいくつあるか。
# 偶数の場合は正解した問題の数が等しくなる可能性がある。
# 奇数の場合は必ず異なる数になる。
#
# 1の個数の偶奇が異なれば等しくなくなる
# 偶数の人×奇数の人
N, M = map(int, input().split())

even = 0
odd = 0
for _ in range(N):
    S = sum(map(int, input()))
    if S % 2:
        odd += 1
    else:
        even += 1
print(even*odd)
