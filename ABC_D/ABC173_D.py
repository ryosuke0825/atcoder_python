N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
syugo = [0]*N
syugo[0] = A[0]
syugo[1] = A[1]
flg = False
ans = A[0]
idx = 1
for i in range(2, N):
    if flg:
        ans += A[idx]
        flg = False
        idx += 1
    else:
        ans += A[idx]
        flg = True

print(ans)
