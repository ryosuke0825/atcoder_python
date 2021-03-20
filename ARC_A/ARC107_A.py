A, B, C = map(int, input().split())
MOD = 998244353
print(((A*B*C*(A+1)*(B+1)*(C+1))//8) % MOD)
