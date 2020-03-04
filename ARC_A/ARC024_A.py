L, R = map(int, input().split())
ll = list(map(int, input().split()))
rl = list(map(int, input().split()))

lsize = [0]*41
rsize = [0]*41
for l in ll:
    lsize[l] += 1
for r in rl:
    rsize[r] += 1

ans = 0
for i in range(10, 41):
    ans += min(lsize[i], rsize[i])
print(ans)
