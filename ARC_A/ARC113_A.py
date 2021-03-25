K = int(input())

flg = False
ans = 0
for a in range(1, K**2+1):
    for b in range(a, K**2+1):
        c = K//(a*b)

        if a == b:
            ans += c
        else:
            ans += c*2

        if c == 0:
            flg = True
            break
    if flg:
        flg = False
        if K < a*2+1:
            break


print(ans)
