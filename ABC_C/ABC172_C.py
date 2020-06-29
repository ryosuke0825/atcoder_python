import itertools
import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

aa = [0] + list(itertools.accumulate(A))
bb = [0] + list(itertools.accumulate(B))

ans = bisect.bisect_left(aa, K)-1
ans = max(ans, bisect.bisect_left(bb, K)-1)

for i in reversed(range(N+1)):
    tmp_K = K-aa[i]
    if tmp_K == 0:
        ans = max(ans, i)
    elif tmp_K < 0:
        continue

    if i + M <= ans:
        continue

    if tmp_K >= bb[-1]:
        ans = max(ans, i+M)
        continue

    ans = max(ans, bisect.bisect_left(bb, tmp_K)-1+i)
print(ans)
