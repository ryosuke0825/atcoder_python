_ = int(input())
v = list(map(float, input().split()))

v.sort()
while True:
    if len(v) > 1:
        new = (v.pop(0)+v.pop(0))/2
        v.append(new)
        v.sort()
    else:
        break

print(v[0])
