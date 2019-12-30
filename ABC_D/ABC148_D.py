N = int(input())
a = list(map(int, input().split()))

flg = False
ret = 0
i = 1
for tmp in a:
    if(i != tmp):
        ret += 1
    else:
        i += 1
        flg = True

if not flg:
    print(-1)
else:
    print(ret)
