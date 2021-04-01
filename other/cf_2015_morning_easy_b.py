N = int(input())
S = input()

if N % 2 != 0:
    print(-1)
    exit(0)

half = N//2
ans = 0
for i in range(half):
    if S[i] != S[i+half]:
        ans += 1
print(ans)
