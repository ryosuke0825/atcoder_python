n, k = map(int, input().split())
h = list(map(int, input().split()))

if n <= k:
    print(0)
else:
    h.sort(reverse=True)
    ret = 0
    for i in h[k:]:
        ret += i
    print(ret)
