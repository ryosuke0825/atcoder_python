n = int(input())
s = input()

if len(s) % 2 == 0:
    print(-1)
    exit()

if s[len(s)//2] != "b":
    print(-1)
    exit()

ans = 0
mid = len(s)//2
for i in range(1, mid+1):
    if i % 3 == 1:
        if s[mid-i] == "a" and s[mid+i] == "c":
            ans += 1
        else:
            ans = -1
            break

    elif i % 3 == 2:
        if s[mid-i] == "c" and s[mid+i] == "a":
            ans += 1
        else:
            ans = -1
            break

    elif i % 3 == 0:
        if s[mid-i] == "b" and s[mid+i] == "b":
            ans += 1
        else:
            ans = -1
            break

print(ans)
