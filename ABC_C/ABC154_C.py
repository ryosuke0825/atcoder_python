n = int(input())
al = list(map(int, input().split()))
tmp = list(set(al))

if len(al) == len(tmp):
    print("YES")
else:
    print("NO")
