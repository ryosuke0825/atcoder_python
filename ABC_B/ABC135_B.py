n = int(input())
pl = list(map(int, input().split()))
pl_sort = sorted(pl)

cnt = 0
for i in range(n):
    if pl[i] != pl_sort[i]:
        cnt += 1

if cnt <= 2:
    print("YES")
else:
    print("NO")
