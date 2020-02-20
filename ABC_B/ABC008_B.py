n = int(input())
ansl = {}
for _ in range(n):
    s = input()
    if s in ansl:
        ansl[s] += 1
    else:
        ansl[s] = 1

ans = ""
max_vote = 0
for k in ansl:
    if max_vote < ansl[k]:
        max_vote = ansl[k]
        ans = k
print(ans)
