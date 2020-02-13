n = int(input())

population = 0
spl = []
for i in range(n):
    spl.append(input().split())
    population += int(spl[i][1])

ans = "atcoder"
for sp in spl:
    if population/2 < int(sp[1]):
        ans = sp[0]
        break
print(ans)
