# 6!は6*5*4*3*2*1
# それぞれを素因数分解すると、3*2*5*2*2*3*2*1となる
# それぞれの個数は5が1個、2が4個、3が2個である
# 選ばない場合もあるので、+1した値をかける
# 2*5*3=30個になる


def prime_factorization(n):
    table = []
    for x in range(2, int(n ** 0.5) + 1):
        while n % x == 0:
            table.append(x)
            n //= x
    if n > 1:
        table.append(n)
    return table


N = int(input())
MOD = 10**9+7

mp = [0]*1000
for i in range(2, N+1):
    pf = prime_factorization(i)
    for p in pf:
        mp[p] += 1

ans = 1
for p in mp:
    if p == 0:
        continue

    ans = ans*(p+1)

print(ans % MOD)
