n = int(input())
ans = n//10*100

if n % 10 <= 6:
    ans += 15*(n % 10)
else:
    ans += 100
print(ans)
