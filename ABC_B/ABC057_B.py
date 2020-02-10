n, m = map(int, input().split())

abl = []
for _ in range(n):
    ab = list(map(int, input().split()))
    abl.append(ab)

cdl = []
for _ in range(m):
    cd = list(map(int, input().split()))
    cdl.append(cd)

print(abl)
print(cdl)
ansl = []
for i, ab in enumerate(abl):
    ans = 10**8
    for cd in cdl:
        ans = min(abs(ab[0]-cd[0]) + abs(ab[1]-cd[1]), ans)
    ansl.append(ans)

for ans in ansl:
    print(ans)
