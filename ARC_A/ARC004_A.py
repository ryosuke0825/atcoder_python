import math

n = int(input())
X = []
Y = []
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        ans = max(ans, (X[i]-X[j])**2+(Y[i]-Y[j])**2)

print(math.sqrt(ans))
