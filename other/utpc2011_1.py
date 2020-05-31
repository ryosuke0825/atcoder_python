import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
ans = 0
for _ in range(N):
    a = list(map(int, input().split()))
    ans = max(ans, a.count(1))
print(ans)
