x = int(input())

if x <= 6:
    print(1)
elif x <= 11:
    print(2)
else:
    ans = (x//11)*2
    if x % 11 != 0:
        ans += 1
    if x % 11 >= 7:
        ans += 1
    print(ans)
