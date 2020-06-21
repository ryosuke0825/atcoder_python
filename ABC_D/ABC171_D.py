from collections import Counter

import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
A = list(map(int, input().split()))
ac = Counter(A)

a_sum = sum(A)
Q = int(input())
for _ in range(Q):
    b, c = map(int, input().split())

    if b in ac:
        a_sum += (c-b)*ac[b]
        ac[c] += ac[b]
        del ac[b]
    print(a_sum)
