import sys


def input():
    return sys.stdin.readline()[:-1]


T = int(input())

for _ in range(T):
    t = int(input())

    if t % 4 == 0:
        print('Even')
    elif t % 2 == 0:
        print('Same')
    else:
        print('Odd')
