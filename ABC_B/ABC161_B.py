N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
miman = sum(A)/(4*M)

for i in range(M):
    if not(A[i] >= miman):
        print('No')
        exit(0)
print('Yes')
