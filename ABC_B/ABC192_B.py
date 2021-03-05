S = input()

ans = 'Yes'
for i in range(len(S)):
    if not(((i+1) % 2 != 0 and S[i].islower()) or ((i+1) % 2 == 0 and S[i].isupper())):
        ans = 'No'
        break
print(ans)
