from fractions import gcd

n = int(input())
A = list(map(int, input().split()))

# 入力が2つなら最大値が解となる
if n == 2:
    print(max(A))
    exit()

# A1 A2 A3の最大公約数はA1とA2の最大公約数とA3の最大公約数と同値になるので、
# 左右から順番に最大公約数を求めていく。
# 初期値を代入する（右からは0番目にAの最初の要素を、左からは末尾にAの末尾の要素）
gcdL = [0]*n
gcdR = [0]*n
gcdL[0] = A[0]
gcdR[-1] = A[-1]

for i in range(1, n):
    gcdL[i] = gcd(gcdL[i-1], A[i])
    gcdR[-i-1] = gcd(gcdR[-i], A[-i-1])

# A0～AiとAi+1～Anの最大公約数を求めていく
# 最大値が解となる
ans = gcdR[1]
for i in range(1, n-1):
    tmp = gcd(gcdL[i-1], gcdR[i+1])
    ans = max(ans, tmp)
ans = max(ans, gcdL[-2])

print(ans)
