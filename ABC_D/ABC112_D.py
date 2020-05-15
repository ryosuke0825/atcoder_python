import math


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors


N, M = map(int, input().split())
divisors = make_divisors(M)
ans = 1
for d in divisors:
    if d*N <= M:
        ans = max(ans, d)
print(ans)
