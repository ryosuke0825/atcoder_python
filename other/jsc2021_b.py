import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dica = collections.Counter(A)
dicb = collections.Counter(B)

ans = []
for a in A:
    if not(a in dicb):
        ans.append(a)

for b in B:
    if not(b in dica):
        ans.append(b)

ans2 = list(set(ans))
ans2.sort()
print(' '.join(map(str, ans2)))
