s = input()
t = int(input())

u = s.count("U")
d = s.count("D")
l = s.count("L")
r = s.count("R")
q = s.count("?")

ans = abs(u-d) + abs(l-r)
if t == 1:
    ans += q
else:
    if ans > q:
        ans -= q
    else:
        if ans % 2 == q % 2:
            ans = 0
        else:
            ans = 1

print(ans)
