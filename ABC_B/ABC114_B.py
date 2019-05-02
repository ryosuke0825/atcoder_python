s = list(map(int, input()))
ans = abs(753-(int(s[0]*100 + s[1]*10 + s[2])))

for i in range(1, len(s)-2):
    tmp = abs(753-(int(s[i]*100 + s[i+1]*10 + s[i+2])))
    if tmp < ans:
        ans = tmp

print(ans)
