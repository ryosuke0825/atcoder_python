def comb(n, k):
    nCk = 1
    MOD = 10**9+7

    for i in range(n-k+1, n+1):
        nCk *= i
        nCk %= MOD

    for i in range(1, k+1):
        nCk *= pow(i, MOD-2, MOD)
        nCk %= MOD
    return nCk


n, a, b = map(int, input().split())
mod = 10**9+7
ans = pow(2, n, mod)-1-comb(n, a)-comb(n, b)
print(ans % mod)
