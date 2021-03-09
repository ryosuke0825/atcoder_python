import math

N = int(input())

ans = 2
for i in range(3, N+1):
    ans = ans * i // math.gcd(ans, i)
print(ans+1)
