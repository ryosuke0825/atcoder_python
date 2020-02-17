n = int(input())
a, b = map(int, input().split())
k = int(input())
pl = list(map(int, input().split()))
pl_set = set(pl)

if a in pl or b in pl or len(pl_set) != len(pl):
    print("NO")
else:
    print("YES")
