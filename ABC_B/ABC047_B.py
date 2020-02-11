w, h, n = map(int, input().split())
whl = [[0 for _ in range(w)] for _ in range(h)]

xyal = []
for _ in range(n):
    xyal.append(list(map(int, input().split())))

for xya in xyal:
    if xya[2] == 1:
        for y in range(h):
            for x in range(xya[0]):
                whl[y][x] = 1

    if xya[2] == 2:
        for y in range(h):
            if xya[0]+1 > w:
                break
            for x in range(xya[0], w):
                whl[y][x] = 1

    if xya[2] == 3:
        for y in range(xya[1]):
            for x in range(w):
                whl[y][x] = 1

    if xya[2] == 4:
        for y in range(xya[1], h):
            for x in range(w):
                whl[y][x] = 1

ans = 0
for wh in whl:
    ans += wh.count(0)
print(ans)
