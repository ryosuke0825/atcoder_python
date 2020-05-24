import sys
from operator import mul
from functools import reduce


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
s_dic = {}
for _ in range(N):
    s_list = list(input())
    s_list.sort()
    s = ''.join(s_list)

    if s in s_dic:
        s_dic[s] += 1
    else:
        s_dic[s] = 1

ans = 0
for v in s_dic.values():
    if v >= 2:
        ans += v*(v-1)
print(ans//2)
