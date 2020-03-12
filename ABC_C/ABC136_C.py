n = int(input())
H = list(map(int, input().split()))

for i in reversed(range(n-1)):
    if H[i] <= H[i+1]:
        continue
    elif H[i]-1 == H[i+1]:
        H[i] -= 1
    else:
        break
else:
    print('Yes')
    exit(0)
print('No')
