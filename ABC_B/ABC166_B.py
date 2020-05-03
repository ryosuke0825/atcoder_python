N, K = map(int, input().split())
sunuke = [0]*N
for _ in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        sunuke[a-1] += 1

ans = 0
for i in range(N):
    if sunuke[i-1] == 0:
        ans += 1
print(ans)
