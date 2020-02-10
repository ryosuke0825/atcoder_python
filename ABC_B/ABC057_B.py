n, m = map(int, input().split())

abl = []
for _ in range(n):
    ab = list(map(int, input().split()))
    abl.append(ab)

cdl = []
for _ in range(m):
    cd = list(map(int, input().split()))
    cdl.append(cd)

ansl = [0 for _ in range(n)]
for i, ab in enumerate(abl):
    ans = 10**10
    for j, cd in enumerate(cdl):
        if abs(ab[0]-cd[0]) + abs(ab[1]-cd[1]) < ans:
            ansl[i] = j
            ans = abs(ab[0]-cd[0]) + abs(ab[1]-cd[1])

for ans in ansl:
    print(ans+1)
