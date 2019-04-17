s=list(input())
ret = ""
for val in s:
    if val == "1":
        ret += "9"
    elif val == "9":
        ret += "1"
    else:
        ret += val
print(ret)