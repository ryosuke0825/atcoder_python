N = int(input())

ans = 0
for i in range(3, 16, 3):
    A = 10**i
    if N >= A:
        ans += N-(A-1)

print(ans)
