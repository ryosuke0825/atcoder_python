a, k = map(int, input().split())

m = 2*10**12
ans = 0

if k == 0:
    print(m-a)
else:
    while True:
        if a >= m:
            print(ans)
            exit(0)
        a += 1+k*a
        ans += 1
