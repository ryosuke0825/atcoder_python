n, m = map(int, input().split())
ansl = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    ansl[a-1] += 1
    ansl[b-1] += 1

for ans in ansl:
    print(ans)
