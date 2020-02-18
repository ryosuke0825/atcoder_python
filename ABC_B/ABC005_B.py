n = int(input())

ans = 100
for _ in range(n):
    t = int(input())
    ans = min(ans, t)

print(ans)
