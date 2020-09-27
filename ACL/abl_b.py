A, B, C, D = map(int, input().split())

ans = 'No'
if A <= C <= B or A <= D <= B:
    ans = 'Yes'
elif C <= A <= D or C <= B <= D:
    ans = 'Yes'
print(ans)
