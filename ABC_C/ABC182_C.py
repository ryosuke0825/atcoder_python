N = list(map(int, input()))
L = len(N)

ans = 100
for i in range(2**L):
    cnt = 0
    sm = 0
    for j in range(L):
        if ((i >> j) & 1):
            sm += N[j]
        else:
            cnt += 1
    if sm != 0 and sm % 3 == 0:
        ans = min(ans, cnt)

if ans == 100:
    ans = -1
print(ans)
