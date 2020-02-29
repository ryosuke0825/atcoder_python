s = input()
rs = s[::-1]
for i in range(len(s)//2):
    if s[i] != rs[i] and not(s[i] == '*' or rs[i] == '*'):
        print('NO')
        break
else:
    print('YES')
