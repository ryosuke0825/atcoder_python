import collections

S = input()
c = collections.Counter(S)

pairs = 0
odd = 0
for v in c.values():
    pairs += v//2
    if v % 2 != 0:
        odd += 1
if odd == 0:
    print(len(S))
else:
    print(1+2*(pairs//odd))
