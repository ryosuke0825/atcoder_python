prize = [0, 300000, 200000, 100000]
x, y = map(int, input().split())

ans = 0
if x <= 3:
    ans += prize[x]
if y <= 3:
    ans += prize[y]
if x == y == 1:
    ans += 400000
print(ans)
