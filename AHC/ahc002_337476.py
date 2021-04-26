si, sj = map(int, input().split())

T = []
for i in range(50):
    t = list(map(int, input().split()))
    T.append(t)

P = []
for i in range(50):
    p = list(map(int, input().split()))
    P.append(p)

chack = [[0] * 50 for i in range(50)]
chack[si][sj] = -1
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for i, j in move:
    if si+i != -1 and si+i != 50 and sj+j != -1 and sj+j != 50:
        if T[si+i][sj+j] == T[si][sj]:
            chack[si+i][sj+j] = -1
            break

ans = [""]*1250
move_s = ["D", "U", "R", "L"]
cnt = 0
move_r = [(1, 0), (-1, 0), (0, 1000), (0, -1)]
move_l = [(1, 0), (-1, 0), (0, 1), (0, -1000)]
rl = 0
while True:
    if sj == 0:
        rl = 1
    elif sj == 49:
        rl = 0
    koho = -1
    mx = -1
    koho_i = -1
    koho_j = -1
    for m in range(4):
        if rl == 0:
            i, j = move_r[m]
        else:
            i, j = move_l[m]

        if si+i > -1 and si+i < 50 and sj+j > -1 and sj+j < 50:
            if chack[si+i][sj+j] != -1:
                if P[si+i][sj+j] > mx:
                    koho = m
                    mx = P[si+i][sj+j]
                    koho_i = i
                    koho_j = j
    if koho == -1:
        break
    si += koho_i
    sj += koho_j
    ans[cnt] = move_s[koho]
    chack[si][sj] = -1
    cnt += 1
    for i, j in move:
        if si+i > -1 and si+i < 50 and sj+j > -1 and sj+j < 50:
            if T[si+i][sj+j] == T[si][sj]:
                chack[si+i][sj+j] = -1
                break

print(''.join(ans))
