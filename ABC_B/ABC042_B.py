n, l = map(int, input().split())
sl = []
for _ in range(n):
    sl.append(input())

sl.sort()
ans = ""
for s in sl:
    ans += s

print(ans)
