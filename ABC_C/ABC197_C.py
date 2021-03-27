N = int(input())
A = list(map(int, input().split()))

# 論理和：|
# 排他的論理和：^
ans = 10**10

# bit全探索で全ての区切り位置を試す。
# 区切り位置なのでN-1となる。
for i in range(2**(N-1)):
    cnt_or = A[0]
    cnt_xor = 0
    # あるパターンの時
    for j in range(N-1):
        # 区間が変わる時、継続する時
        if ((i >> j) & 1):
            # 区間が変わるので排他的論理和を求める
            cnt_xor ^= cnt_or
            cnt_or = A[j+1]
        else:
            # 同じ区間内なので論理和と求める
            cnt_or |= A[j+1]
    # 最後の区間分の論理和を使って排他的論理和を求める
    cnt_xor ^= cnt_or
    # 最小値の更新
    ans = min(ans, cnt_xor)

print(ans)
