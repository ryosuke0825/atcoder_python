from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


S = list(input())

# それぞれの記号の個数を求める
used = 0
unused = 0
unknow = 0
for s in S:
    if s == 'o':
        used += 1
    elif s == 'x':
        unused += 1
    else:
        unknow += 1

# 0通りの場合
if used >= 5 or (used+unknow) == 0:
    print(0)
    exit()

ans = 0
# ?を0個～全部使う場合を全て求める
for add in range(0, unknow+1):
    cnt = used+add
    if cnt == 1:
        ans += 1*cmb(unknow, add)
    elif cnt == 2:
        ans += (2*4+cmb(4, 2))*cmb(unknow, add)
    elif cnt == 3:
        ans += (3*4*3*cmb(unknow, add))
    elif cnt == 4:
        ans += (4*3*2*cmb(unknow, add))
print(ans)
