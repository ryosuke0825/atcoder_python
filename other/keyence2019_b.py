s = input()
for i in range(8):
    if s[:i]+s[len(s)-(7-i):] == 'keyence':
        print('YES')
        exit(0)
print('NO')
