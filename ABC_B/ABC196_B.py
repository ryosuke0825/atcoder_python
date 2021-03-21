X = input()

ans = X
if X.find(".") != -1:
    ans = X[0:X.find(".")]
print(ans)
