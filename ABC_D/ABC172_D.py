N = int(input())

ans = 0
for i in range(1, N+1):
    tmp = i*(N//i)
    ans += (N//i)*(tmp+i)//2
print(ans)
