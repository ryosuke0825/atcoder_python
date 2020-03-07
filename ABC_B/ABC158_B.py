n, a, b = map(int, input().split())

ans = n//(a+b)*a
amari = n-(a+b)*(n//(a+b))
ans += min(amari, a)

print(ans)
