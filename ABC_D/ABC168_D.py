import sys


def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
tree = [[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

ans = [0]*(N-1)
next_root = [0]
zumi = {}
while True:
    # 次のルートが全部探索済みなら終わり
    for root in next_root:
        if not(root in zumi):
            break
    else:
        break

    tmp_next_root = []
    for root in next_root:
        if root in zumi:
            continue
        for v in tree[root]:
            if v in zumi:
                continue
            if ans[v-1] == 0:
                ans[v-1] = root+1
                tmp_next_root.append(v)
        zumi[root] = True
    next_root = tmp_next_root

if ans.count(0) == 0:
    print('Yes')
    for a in ans:
        print(a)
else:
    print('No')
