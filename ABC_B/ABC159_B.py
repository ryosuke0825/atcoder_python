s = input()
rs = s[::-1]

# 回文チェック
for i in range(len(s)):
    if s[i] != rs[i]:
        print('No')
        exit(0)

# 前半の回文チェック
zs = s[:len(s)//2]
rzs = zs[::-1]
for i in range(len(zs)):
    if zs[i] != rzs[i]:
        print('No')
        exit(0)

# 後半の回文チェック
ks = s[len(s)//2+1:]
rks = ks[::-1]
for i in range(len(ks)):
    if ks[i] != rks[i]:
        print('No')
        exit(0)

print('Yes')
