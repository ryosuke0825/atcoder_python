n = int(input())
if n % 20 == 0:
    if n // 20 % 2 == 0:
        print(1)
    else:
        print(20)
else:
    if n // 20 % 2 == 0:
        print(n % 20)
    else:
        print(21-n % 20)
