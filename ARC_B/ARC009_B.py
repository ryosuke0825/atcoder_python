B = input().split()
N = int(input())

ans = [[''] * 2 for i in range(N)]
for i in range(N):
    A = input()
    convert = ''
    for a in A:
        convert = convert + str(B.index(a))
    ans[i][0] = int(convert)
    ans[i][1] = A

ans.sort()
for i in range(N):
    print(ans[i][1])
