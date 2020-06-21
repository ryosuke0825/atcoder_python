N = int(input())

ans = ''
while True:
    amari = N % 26
    N = N//26

    if amari == 0:
        ans = 'z'+ans
        N -= 1
    else:
        ans = chr(96+amari)+ans

    if N == 0:
        break

print(ans)
