n, m = map(int, input().split())

al = []
for _ in range(n):
    al.append(list(input()))

bl = []
for _ in range(m):
    bl.append(list(input()))

flag1 = False
for ax in range(n-m+1):
    for ay in range(n-m+1):

        flag2 = True
        for bx in range(m):
            for by in range(m):
                if al[ax+bx][ay+by] != bl[bx][by]:
                    flag2 = False
        if flag2:
            flag1 = True

if flag1:
    print("Yes")
else:
    print("No")
