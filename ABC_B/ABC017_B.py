x = input()
cnt = x.count('o')
cnt += x.count('k')
cnt += x.count('u')
cnt += x.count('ch')*2

if cnt == len(x):
    print('YES')
else:
    print('NO')
