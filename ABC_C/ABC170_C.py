from collections import Counter

X, N = map(int, input().split())
P = list(map(int, input().split()))
c = Counter(P)

if not(X in c):
    print(X)
    exit(0)

for i in range(200):
    tmp1 = X-i
    if not(tmp1 in c):
        print(tmp1)
        exit(0)

    tmp2 = X+i
    if not(tmp2 in c):
        print(tmp2)
        exit(0)
