Y = int(input())

ans = 'NO'
if Y % 400 == 0:
    ans = 'YES'
elif Y % 4 == 0 and Y % 100 != 0:
    ans = 'YES'
print(ans)
