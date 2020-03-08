n = int(input())
k = int(input())
xl = map(int, input().split())

ans = 0
for x in xl:
    a = x*2
    b = abs(k-x)*2
    ans += min(a, b)
print(ans)
