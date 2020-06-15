from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
p = [True]*(10**6+1)

for k, v in c.items():
    t = k*2
    while t <= 10**6:
        p[t] = False
        t += k

ans = 0
for a in A:
    if c[a] == 1 and p[a]:
        ans += 1
print(ans)
