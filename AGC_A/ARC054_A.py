L, X, Y, S, D = map(int, input().split())

if S == D:
    print(0)
    exit(0)

kyori = 0
rkyori = 0
if S < D:
    kyori = D-S
    rkyori = S+(L-D)
else:
    kyori = (L-S)+D
    rkyori = S-D

time = kyori/(X+Y)
if X >= Y:
    print(time)
else:
    rtime = rkyori/(Y-X)
    print(min(time, rtime))
