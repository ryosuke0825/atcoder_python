import collections

N = int(input())
A = list(map(int, input().split()))

c = collections.Counter(A)
ans = 0
for k, v in c.items():
    if k == v:
        continue
    elif k < v:
        ans += v-k
    else:
        ans += v
print(ans)
