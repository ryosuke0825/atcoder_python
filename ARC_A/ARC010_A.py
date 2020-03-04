n, m, a, b = map(int, input().split())

if n <= a:
    n += b

for i in range(m):
    c = int(input())
    n -= c
    if n < 0:
        print(i+1)
        exit(0)

    if n <= a:
        n += b

print('complete')
