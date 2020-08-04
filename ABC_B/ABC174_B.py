import sys
import math


def input():
    return sys.stdin.readline()[:-1]


N, D = map(int, input().split())
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    if math.sqrt(x**2+y**2) <= D:
        ans += 1
print(ans)
