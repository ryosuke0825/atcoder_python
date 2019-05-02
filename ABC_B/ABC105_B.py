N = int(input())
C = int(N / 4)
D = int(N / 7)
ans = "No"
for c in range(0, C+1):
    for d in range(0, D+1):
        if c*4 + d*7 == N:
            ans = "Yes"
print(ans)
