s = input()

ans = ""
for word in s:
    if word == "0":
        ans += "0"
    elif word == "1":
        ans += "1"
    else:
        if ans != "":
            ans = ans[:-1]

print(ans)
