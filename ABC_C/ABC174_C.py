K = int(input())

seven = 7
ans = -1
for i in range(K):
    if seven % K == 0:
        ans = i+1
        break
    seven = (seven*10+7) % K
print(ans)
