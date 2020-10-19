N = int(input())

a, b = map(int, input().split())
ans = 0
for _ in range(N-1):
    c, d = map(int, input().split())
    ans += abs(a-c)+abs(b-d)

    a, b = c, d
print(ans)
