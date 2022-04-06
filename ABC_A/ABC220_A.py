A, B, C = map(int, input().split())

ans = C
while True:
    if A <= ans <= B:
        print(ans)
        break
    ans += C
    if B < ans:
        print(-1)
        break
