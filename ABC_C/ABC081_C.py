import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))

AC = collections.Counter(A)

if K >= len(AC):
    print(0)
    exit(0)

delete_item_num = len(AC)-K
ans = 0
cnt = 0
for k, v in sorted(AC.items(), key=lambda x: x[1]):
    cnt += 1
    ans += v
    if cnt >= delete_item_num:
        print(ans)
        exit(0)
