from bisect import bisect_left

D = int(input())
N = int(input())
M = int(input())

shop = [0]*N
for i in range(1, N):
    shop[i] = int(input())
shop.sort()

target = [0]*M
for i in range(M):
    target[i] = int(input())
#print('shop', shop)
#print('target', target)

ans = 0
for m in target:
    koho_shop = bisect_left(shop, m)
    #print("koho_shop", koho_shop)
    if koho_shop == N:
        ans += min(D-m, abs(m-shop[koho_shop-1]))
    else:
        ans += min(abs(m-shop[koho_shop]), abs(m-shop[koho_shop-1]))
print(ans)
