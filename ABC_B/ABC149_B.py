A, B, K = map(int, input().split())

if(A >= K):
    print(str(A-K) + " " + str(B))
elif(A+B >= K):
    ret = B-(K-A)
    print(str(0) + " " + str(ret))
else:
    print("0 0")
