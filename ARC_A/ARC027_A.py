h, m = map(int, input().split())

ans = 0
if h < 17:
    ans = (17-h)*60
print(ans+(60-m))
