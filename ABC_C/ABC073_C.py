N = int(input())

ans = {}
for _ in range(N):
    a = input()
    if a in ans:
        del ans[a]
    else:
        ans[a] = 1

print(len(ans))
