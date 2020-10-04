from collections import defaultdict

N, S = input().split()
N = int(N)

cnt = defaultdict(int)
cntchr = defaultdict(int)

cnt[(0, 0)] = 1
ans = 0

for i in range(N):
    cntchr[S[i]] += 1
    AminusT = cntchr['A']-cntchr['T']
    CminusG = cntchr['C']-cntchr['G']
    ans += cnt[(AminusT, CminusG)]
    cnt[(AminusT, CminusG)] += 1

print(ans)
