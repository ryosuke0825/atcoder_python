N = int(input())

ans = 0
for i in range(1, N):
    ans += max((N-1)//i, 1)
print(ans)
