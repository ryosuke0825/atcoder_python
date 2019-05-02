N, M = map(int, input().split())
K = []
for i in range(N):
    tmp = list(map(int, input().split()))
    del tmp[0]
    K.append(tmp)

ans = K[0][:]
for i in range(1, N):
    ans = list(set(ans) & set(K[i]))

print(len(ans))
