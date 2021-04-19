A, B = map(int, input().split())

ans = []
if A == B:
    for i in range(1, A+1):
        ans.append(i)
        ans.append(i*-1)

elif A > B:
    for i in range(1, A+1):
        ans.append(i)
    tmp = 0
    for i in range(1, A+1):
        if B > i:
            ans.append(i*-1)
        else:
            tmp += i
    ans.append(tmp*-1)

else:
    for i in range(1, B+1):
        ans.append(i*-1)
    tmp = 0
    for i in range(1, B+1):
        if A > i:
            ans.append(i)
        else:
            tmp += i
    ans.append(tmp)

print(' '.join(map(str, ans)))
