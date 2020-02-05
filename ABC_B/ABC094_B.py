n, m, x = map(int, input().split())
al = list(map(int, input().split()))

right_route = 0
for i in range(x, n+1):
    if i in al:
        right_route += 1

left_route = 0
for i in reversed(range(1, x+1)):
    if i in al:
        left_route += 1

print(min(right_route, left_route))
