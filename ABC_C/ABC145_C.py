import itertools
import math
import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
XY = []
for _ in range(N):
    x, y = map(int, input().split())
    XY.append([x, y])

sum_distance = 0
for x, y in list(itertools.combinations(range(N), 2)):
    sum_distance += math.sqrt(abs(XY[x][0]-XY[y][0])**2+abs(XY[x][1]-XY[y][1])**2)
print(sum_distance/(N/2))
