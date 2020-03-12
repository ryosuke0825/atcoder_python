n = int(input())
H = list(map(int, input().split()))

bh = H[0]
for i in range(1, len(H)):
    if H[i] == bh:
        continue
    elif H[i] > bh:
        bh = H[i]
    elif H[i]-1 == bh:
        continue
    else:
        break
else:
    print('Yes')
    exit(0)
print('No')
