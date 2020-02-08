h, w = map(int, input().split())
hwl = []
for _ in range(h):
    l = list(input())
    hwl.append(l)

for i in range(h):
    for j in range(w):
        if hwl[i][j] == ".":
            cnt = 0
            if i != 0 and j != 0 and hwl[i-1][j-1] == "#":
                cnt += 1
            if i != 0 and hwl[i-1][j] == "#":
                cnt += 1
            if i != 0 and j < w-1 and hwl[i-1][j+1] == "#":
                cnt += 1
            if j != 0 and hwl[i][j-1] == "#":
                cnt += 1
            if j < w-1 and hwl[i][j+1] == "#":
                cnt += 1
            if i < h-1 and j != 0 and hwl[i+1][j-1] == "#":
                cnt += 1
            if i < h-1 and hwl[i+1][j] == "#":
                cnt += 1
            if i < h-1 and j < w-1 and hwl[i+1][j+1] == "#":
                cnt += 1
            hwl[i][j] = str(cnt)
    print("".join(hwl[i]))
