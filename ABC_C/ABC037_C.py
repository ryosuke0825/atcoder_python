N, K = map(int, input().split())
A = list(map(int, input().split()))

sum_tmp = sum(A[:K])
ans = sum_tmp
for i in range(K, N):
    sum_tmp = sum_tmp-A[i-K]+A[i]
    ans += sum_tmp
print(ans)
