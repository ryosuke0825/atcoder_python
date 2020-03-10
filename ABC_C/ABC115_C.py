n, k = map(int, input().split())

hl = []
for _ in range(n):
    hl.append(int(input()))

hl.sort()

ans = 10**9+1
for i in range(len(hl)-k+1):
    ans = min(ans, hl[i+k-1]-hl[i])

print(ans)
