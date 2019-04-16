a, b = map(int, input().split())
coin = 0

if a == b:
    coin = a + b
else:
    if a > b:
        coin = a
        a -= 1
    elif b > a:
        coin = b
        b -= 1

    if a > b:
        coin += a
        a -= 1
    elif b > a:
        coin += b
        b -= 1
    else:
        coin += a

print(coin)