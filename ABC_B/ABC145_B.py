n = int(input())
s = list(input())

if n % 2 != 0:
    print("No")
else:
    if s[n//2:] == s[:n//2]:
        print("Yes")
    else:
        print("No")
