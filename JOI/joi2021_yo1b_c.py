N = int(input())
A = list(map(int, input().split()))

mx = max(A)
idx = A.index(mx)

if idx == 0:
    print(0)
    print(sum(A[idx+1:]))
elif idx == len(A)-1:
    print(sum(A[:idx]))
    print(0)
else:
    print(sum(A[:idx]))
    print(sum(A[idx+1:]))
