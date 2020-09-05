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

ans = [[] for i in range(N)]
for target_no in range(N):
    for t_friend_no in tree[target_no]:
        for t_friend_friend_no in tree[t_friend_no]:
            if target_no == t_friend_friend_no:
                continue
            if t_friend_friend_no in tree[target_no]:
                continue
            if t_friend_friend_no in ans[target_no]:
                continue
            ans[target_no].append(t_friend_friend_no)

for a in ans:
    print(len(a))
