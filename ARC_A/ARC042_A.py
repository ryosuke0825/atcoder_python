import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
A = [-1]*M
for i in range(M):
    A[i] = int(input())

ans = []
ans_s = set()
for i in reversed(range(M)):
    if not(A[i] in ans_s):
        ans.append(A[i])
        ans_s.add(A[i])

for i in range(1, N+1):
    if not(i in ans_s):
        ans.append(i)

for i in range(N):
    print(ans[i])
