import heapq
import fractions


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            while temp % i == 0:
                arr.append(i)
                temp //= i

    if temp != 1:
        arr.append(temp)

    if arr == []:
        arr.append(n)

    arr.sort()
    return arr


N, P = map(int, input().split())

# リストを優先度付きキューへ
factors = factorization(P)
heapq.heapify(factors)

# 因数の数がNより少ないなら1になる
if len(factors) < N:
    print(1)
    exit(0)

# 因数の数がNと一致するなら最小値の因数が解になる
if len(factors) == N:
    print(min(factors))
    exit(0)

# 因数の数がNより大きい時、
# 因数の数がNとおなじになるまで、小さい値同士を掛ける。
# 同じ値になったら最小値を出力する。
ans = []
while True:
    if len(ans) < N:
        ans.append(heapq.heappop(factors))
    else:
        if len(factors) == 0:
            break

        idx = ans.index(min(ans))
        ans[idx] = ans[idx]*heapq.heappop(factors)

if N == 1:
    print(ans[0])
else:
    gcd = fractions.gcd(ans[0], ans[1])
    if N == 2:
        print(gcd)
    else:
        for i in range(2, N):
            gcd = fractions.gcd(gcd, ans[i])
        print(gcd)
