a, b, c = map(int, input().split())

ba = a
bb = b
bc = c
ans = 0
while True:
    if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
        break

    if a == b == c:
        ans = -1
        break
    ta = a//2
    tb = b//2
    tc = c//2
    a = tb+tc
    b = ta+tc
    c = ta+tb
    ans += 1

print(ans)
