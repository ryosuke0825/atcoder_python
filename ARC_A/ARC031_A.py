name = input()
name1 = name[::-1]
for i in range(len(name)):
    if name[i] != name1[i]:
        print('NO')
        break
else:
    print('YES')
