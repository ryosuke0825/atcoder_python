n = list(input())

if n[0] != '9':
    if n.count('9') != len(n)-1:
        n[0] = str(int(n[0])-1)
        for i in range(1, len(n)):
            n[i] = '9'

else:
    for i in range(len(n)-1):
        if n[i+1] != '9':
            n[i] = str(int(n[i])-1)
            for j in range(i+1, len(n)):
                n[j] = '9'

ans = 0
for i in range(len(n)):
    ans += int(n[i])
print(ans)
