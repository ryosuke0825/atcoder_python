N = int(input())
A = list(map(int, input().split()))

plus = False
minus = False
ans = 0
for i in range(N-1):
    if not(plus) and not(minus):
        if A[i] < A[i+1]:
            plus = True
        elif A[i] > A[i+1]:
            minus = True

    else:
        if plus:
            if A[i] <= A[i+1]:
                continue
            else:
                ans += 1
                plus = False
        else:
            if A[i] >= A[i+1]:
                continue
            else:
                ans += 1
                minus = False
print(ans+1)
