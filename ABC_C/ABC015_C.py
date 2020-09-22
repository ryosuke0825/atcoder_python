from itertools import product

N, K = map(int, input().split())
T = []
for _ in range(N):
    t = list(map(int, input().split()))
    T.append(t)

for p in product(*T):
    xor = 0
    for i in range(N):
        xor ^= p[i]
    if xor == 0:
        print('Found')
        exit()
print('Nothing')
