n = int(input())
A = list(map(int, input().split()))

ca = [0]
da = {'0': 1}
for i in range(n):
    ca.append(A[i]+ca[i])

    if str(ca[i+1]) in da:
        da[str(ca[i+1])] = da[str(ca[i+1])]+1
    else:
        da[str(ca[i+1])] = 1

ans = 0
for k in da:
    ans += da[k]*(da[k]-1)//2
print(ans)
