import collections

N = int(input())
S = []
for _ in range(N):
    s = input()
    S.append(s)

c = collections.Counter(S)
print(len(c))
