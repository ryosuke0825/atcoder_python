N, S, D = map(int, input().split())
XY = [list(map(int, input().split())) for i in range(N)]

ans = 'No'
for x, y in XY:
    if x < S and y > D:
        ans = 'Yes'
        break
print(ans)
