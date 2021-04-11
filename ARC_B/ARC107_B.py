N, K = map(int, input().split())
K = abs(K)

# 0～N+2までの各値を1～Nで作る時に何通りあるか調べる
# ex N=6 2→(1,1)  ex 11→(6,5)(5,6)
num = [0]*(N*2+1)
for i in range(2, N*2+1):
    num[i] = min(i-1, N*2+1-i)

# Kを作る数は、a+b(num[i])の数×c-d（num[i-K]）の数
#  ex N=6 K=3 i=5 4(num[i])×1(num[i-K])=4 (3,2,1,1),(2,3,1,1),(4,1,1,1),(1,4,1,1)
ans = 0
for i in range(K, N*2+1):
    ans += num[i]*num[i-K]

print(ans)
