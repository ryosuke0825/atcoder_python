a, b = map(int, input().split())

al = []
for i in range(1, 10001):
    if int(i * 0.08) == a:
        al.append(i)
    elif int(i * 0.08) > a:
        break

bl = []
for i in range(1, 10001):
    if int(i * 0.1) == b:
        bl.append(i)
    elif int(i * 0.1) > b:
        break

for aa in al:
    for bb in bl:
        if aa == bb:
            print(aa)
            exit(0)
else:
    print(-1)
