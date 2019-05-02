n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = []
for i in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)
ret = 0
for a1 in a:
    source_sum = 0
    for i in range(len(a1)):
        source_sum += a1[i]*b[i]
    if source_sum + c > 0:
        ret += 1
print(ret)
