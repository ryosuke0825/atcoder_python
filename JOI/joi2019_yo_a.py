import math

A, B, C = map(int, input().split())

ans, amari = divmod(C, (A*7+B))
ans *= 7

if amari > A*7:
    ans += 7
else:
    ans += math.ceil(amari/A)
print(ans)
