import sys


def input():
    return sys.stdin.readline()[:-1]


N, A, B = map(int, input().split())
S = [0]*N
for i in range(N):
    S[i] = int(input())

mean = sum(S)/N
if max(S) == min(S):
    print(-1)
else:
    p = B/(max(S)-min(S))
    q = A-p*mean
    print(p, q)
