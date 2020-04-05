def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


N, X = map(int, input().split())
xl = list(map(int, input().split()))

if N == 1:
    print(abs(X-xl[0]))
    exit(0)

xl.append(X)
xl.sort()

k = []
for i in range(1, N+1):
    tmp = xl[i]-xl[i-1]
    if not(tmp in k):
        k.append(tmp)

if len(k) == 1:
    print(k[0])
elif len(k) == 2:
    ans = gcd(k[0], k[1])
    print(ans)
else:
    ans = gcd(k[0], k[1])
    for i in range(2, len(k)):
        ans = gcd(ans, k[i])
    print(ans)
