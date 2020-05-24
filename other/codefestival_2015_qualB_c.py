N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

if N < M:
    print('NO')
    exit(0)

for i in range(M):
    if A[i] < B[i]:
        print('NO')
        exit(0)
print('YES')
