from collections import Counter

N = int(input())
A = map(int, input().split())
MOD = 10**9+7
ac = Counter(A)

ans = 0
if N % 2 != 0:
    if ac[0] != 1:
        print(0)
        exit(0)
    for i in range(2, N, 2):
        if ac[i] != 2:
            print(0)
            exit(0)
    ans = 2**((N-1)//2)
else:
    for i in range(1, N, 2):
        if ac[i] != 2:
            print(0)
            exit(0)
    ans = 2**(N//2)
print(ans % MOD)
