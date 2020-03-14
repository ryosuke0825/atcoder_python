h, w = map(int, input().split())

ans = 0
if h == 1 or w == 1:
    ans = 1
else:
    if w % 2 == 0:
        ans += (w//2)*h
    else:
        if h % 2 == 0:
            ans += (h//2)*(w//2*2+1)
        else:
            ans += (h//2)*(w//2*2+1)+(w//2+1)
print(max(1, ans))
