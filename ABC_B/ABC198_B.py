N = input()

if N == '0':
    print('Yes')
    exit(0)

while True:
    if N[-1] == '0':
        N = N[:-1]
    else:
        break

if N == N[::-1]:
    print('Yes')
else:
    print('No')
