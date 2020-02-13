s = input()
k = int(input())

ans = []
for i in range(len(s)-k+1):
    if not(s[i:i+k] in ans):
        ans.append(s[i:i+k])

print(len(ans))
