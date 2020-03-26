import math

n = int(input())
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

ans = 0
for x1, y1 in xy:
    for x2, y2 in xy:
        ans += math.sqrt((x1-x2)**2 + (y1-y2)**2)
print(ans/n)
