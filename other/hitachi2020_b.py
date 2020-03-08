A, B, M = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

ans = min(al) + min(bl)
for _ in range(M):
    a, b, m = list(map(int, input().split()))
    ans = min(ans, al[a-1]+bl[b-1]-m)
print(ans)
