n = int(input())
a = list(map(int, input().split()))

rank = [0]*(n+1)
for i in range(1, n+1):
    rank[a[i-1]] = i

ans = ""
for r in rank[1:]:
    if ans != "":
        ans += " "
    ans += str(r)

print(ans)
