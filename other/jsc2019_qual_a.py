M, D = map(int, input().split())

ans = 0
for m in range(1, M+1):
    for d in range(10, D+1):
        d1 = int(str(d)[0])
        d10 = int(str(d)[1])
        if d1 >= 2 and d10 >= 2 and d1*d10 == m:
            ans += 1
print(ans)
