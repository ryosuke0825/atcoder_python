n, k = map(int, input().split())
ans = ""
while True:
    ans = ans+str(n % k)
    n = n//k
    if n == 0:
        break
print(len(ans))
