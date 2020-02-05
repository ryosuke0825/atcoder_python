s = input()

ans = True
for i in range(len(s)):
    if (i+1) % 2 == 0:
        if not(s[i] in ["L", "U", "D"]):
            ans = False

    else:
        if not(s[i] in ["R", "U", "D"]):
            ans = False

if ans:
    print("Yes")
else:
    print("No")
