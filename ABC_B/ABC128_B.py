N = int(input())
SP = []
for i in range(1,N+1):
    tmp =[]
    S_tmp,P_tmp = input().split()
    tmp.append(S_tmp)
    tmp.append(int(P_tmp))
    tmp.append(i)
    SP.append(tmp)

SP.sort()

tmp = []
for i in range(N):
    if (len(tmp)==0):
        tmp.append(SP[i])
    elif(tmp[0][0]==SP[i][0]):
        tmp.append(SP[i])
    else:
        tmp.sort(reverse=True,key=lambda x: x[1])
        for j in (tmp):
            print(j[2])
        #print(tmp)
        tmp = []
        tmp.append(SP[i])

tmp.sort(reverse=True,key=lambda x: x[1])
for j in (tmp):
            print(j[2])
#print(tmp)