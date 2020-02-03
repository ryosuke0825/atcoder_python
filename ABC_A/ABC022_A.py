n, s, t = map(int, input().split())
w = int(input())
ret = 0

if s <= w <= t:
    ret += 1

for _ in range(n-1):
    w += int(input())
    if s <= w <= t:
        ret += 1
print(ret)
