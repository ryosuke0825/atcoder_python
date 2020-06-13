import sys


def input():
    return sys.stdin.readline()[:-1]


C = int(input())
nml = [0, 0, 0]
for _ in range(C):
    tmp = list(map(int, input().split()))
    tmp.sort()

    nml[0] = max(nml[0], tmp[0])
    nml[1] = max(nml[1], tmp[1])
    nml[2] = max(nml[2], tmp[2])

print(nml[0]*nml[1]*nml[2])
