n = int(input())
li = []
for i in range(2):
    tmp = list(map(int, input().split()))
    li.append(tmp)

ret = 0
for i in range(n):
    cost = li[0][i] - li[1][i]
    if cost > 0:
        ret += cost

print(ret)
