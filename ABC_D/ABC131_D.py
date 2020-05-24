import sys


def input():
    return sys.stdin.readline()[:-1]


N = int(input())
BA = []
for _ in range(N):
    a, b = map(int, input().split())
    BA.append([b, a])
BA.sort()

sum_time = 0
for i in range(N):
    sum_time += BA[i][1]
    if sum_time > BA[i][0]:
        print('No')
        exit(0)
print('Yes')
