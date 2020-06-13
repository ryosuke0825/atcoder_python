from collections import Counter

na, nb = map(int, input().split())
A = input().split()
B = input().split()

ac = Counter(A)
bc = Counter(B)

r = 0
for a in A:
    if a in bc:
        r += 1

p = len(A)
for b in B:
    if not(b in ac):
        p += 1

print(r/p)
