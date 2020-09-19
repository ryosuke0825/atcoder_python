N = int(input())

D = []
for _ in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        D.append(True)
    else:
        D.append(False)

for i in range(N-2):
    if D[i] and D[i+1] and D[i+2]:
        print('Yes')
        exit(0)
print('No')
