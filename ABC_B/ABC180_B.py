import math

N = int(input())
X = list(map(int, input().split()))

m, y, c = 0, 0, 0
for x in X:
    c = max(c, abs(x))
    x = abs(x)
    m += x
    y += x**2
print(m)
print(math.sqrt(y))
print(c)
