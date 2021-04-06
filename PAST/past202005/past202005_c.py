A, R, N = map(int, input().split())

if R == 1:
    print(A)
    exit(0)

if N >= 31:
    print('large')
    exit(0)

LIMID = 10**9
ans = A*R**(N-1)
if ans <= LIMID:
    print(ans)
else:
    print('large')
