n, x = map(int, input().split())
al = list(map(int, input().split()))

bin_n = bin(x)
str_bin_n = str(bin_n)[2:]

# 先頭に0を付与して反転させる
str_bin_n = str_bin_n.zfill(n)
str_bin_n = str_bin_n[::-1]

ans = 0
for i, j in enumerate(str_bin_n):
    if j == "1":
        ans += al[i]
print(ans)
