N = int(input())
L = list(map(int, input().split()))

L.sort()
ans = 0
for i in range(0, N*2, 2):
    ans += L[i]
print(ans)
