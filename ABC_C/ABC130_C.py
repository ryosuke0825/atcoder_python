W, H, x, y = map(int, input().split())

if W/2 == x and H/2 == y:
    ans = 1
else:
    ans = 0
print(W*H/2, ans)
