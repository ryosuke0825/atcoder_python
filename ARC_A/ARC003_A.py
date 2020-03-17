n = int(input())
R = list(input())

ans_sum = 0
for r in R:
    if r == 'A':
        ans_sum += 4
    elif r == 'B':
        ans_sum += 3
    elif r == 'C':
        ans_sum += 2
    elif r == 'D':
        ans_sum += 1
print(ans_sum/len(R))
