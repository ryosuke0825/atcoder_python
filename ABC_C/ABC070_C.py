import sys
import math


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
ans = 0
for _ in range(N):
    if ans == 0:
        ans = int(input())
    else:
        t = int(input())
        ans = (ans * t) // math.gcd(ans, t)
print(ans)
