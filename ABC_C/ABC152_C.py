n = int(input())
p = list(map(int, input().split()))

ret = 1
min_num = p[0]
for i in range(1, n):
    if min_num > p[i]:
        ret += 1
        min_num = p[i]

print(ret)
