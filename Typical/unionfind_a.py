import sys


def input():
    return sys.stdin.readline()[:-1]


class UnionFind:
    def __init__(self, N):
        self.root = list(range(N + 1))
        self.size = [1] * (N + 1)

    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            x, y = y, x
            sx, sy = sy, sx
        self.root[y] = x
        self.size[x] += sy


N, Q = map(int, input().split())
pab = []
for _ in range(Q):
    tmp = list(map(int, input().split()))
    pab.append(tmp)

uf = UnionFind(N)
ans = []
for p, a, b in pab:
    if not p:
        uf.merge(a, b)
    else:
        if uf[a] == uf[b]:
            ans.append('Yes')
        else:
            ans.append('No')

print('\n'.join(ans))
