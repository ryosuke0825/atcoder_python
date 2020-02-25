n, l = map(int, input().split())
S = list(input())

ans = 0
tab = 1
for s in S:
    if s == '+':
        tab += 1
        if tab > l:
            ans += 1
            tab = 1
    else:
        tab -= 1

print(ans)
