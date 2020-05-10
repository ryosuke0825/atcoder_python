A, B, C, K = map(int, input().split())

if A >= K:
    print(K)
elif (A+B) >= K:
    print(A)
else:
    tmp = K-(A+B)
    print(A-tmp)
