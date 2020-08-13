n, m = map(int, input().split())
s = []
cums = [0]
for i in range(n-1):
    s.append(int(input()))
    cums.append(cums[i]+s[i])

ans = 0
position = 0
for i in range(m):
    k = int(input())
    # 進む場合
    if k > 0:
        ans += cums[position+k]-cums[position]
    # 戻る場合
    elif k < 0:
        ans += cums[position]-cums[position+k]
    position += k
mad=10**5
print(ans % mad)
