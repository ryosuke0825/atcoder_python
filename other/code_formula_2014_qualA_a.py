a = int(input())
for i in range(101):
    if i**3 == a:
        print('YES')
        exit(0)
print('NO')
