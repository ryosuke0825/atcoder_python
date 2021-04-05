from math import ceil

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 青マスが0の場合はNマスのハンコを作り1回押す
if M == 0:
    print(1)
    exit(0)

A.sort()
space = [0]*(M+1)
K = 10**9

# 最初の青マスまでの白マスの数
if A[0] != 1:
    K = A[0]-1
    space[0] = A[0]-1

for i in range(M-1):
    tmp_mn = A[i+1]-A[i]-1
    # 0の場合＝青マスが連続している場合は更新しない
    if tmp_mn != 0:
        K = min(K, tmp_mn)
    space[i+1] = tmp_mn

# 最後の青マスから末尾までの白マスの数
if A[-1] != N:
    tmp_mn = N-A[-1]
    K = min(K, tmp_mn)
    space[-1] = tmp_mn

# ハンコを何回押すか求める
ans = 0
for s in space:
    if s == 0:
        continue

    ans += ceil(s/K)
print(ans)
