n = int(input())
ans = 0
for _ in range(n):
    a, b, c, d, e = map(int, input().split())
    ans = max(ans, a+b+c+d+(e*11/90))
print(ans)
