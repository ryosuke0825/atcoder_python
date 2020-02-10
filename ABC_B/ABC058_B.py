o = input()
e = input()

ans = ""
for i in range(len(o)):
    ans += o[i]
    if len(e)-1 >= i:
        ans += e[i]
print(ans)
