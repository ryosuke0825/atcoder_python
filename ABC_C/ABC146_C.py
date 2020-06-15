A, B, X = map(int, input().split())

if A+B > X:
    print(0)
    exit(0)

hi = 10**9
lo = 1
ans = hi//2
while True:
    if A*ans+B*len(str(ans)) <= X:
        lo = ans
    else:
        hi = ans
    if ans == (lo+hi)//2:
        if A*(ans+1)+B*len(str(ans+1)) <= X:
            print(ans+1)
        else:
            print(ans)
        exit(0)
    ans = (lo+hi)//2
