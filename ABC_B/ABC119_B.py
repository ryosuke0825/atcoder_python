n = int(input())
xy = []
ret = 0
for i in range(n):
    tmp = input().split()
    if tmp[1] == "JPY":
        ret += float(tmp[0])
    else:
        ret += float(tmp[0])*380000

print(ret)
