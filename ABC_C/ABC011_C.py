N = int(input())
ng1 = int(input())
ng2 = int(input())
ng3 = int(input())

ng_list = [ng1, ng2, ng3]
ng_list.sort()

if N in ng_list:
    print('NO')
    exit(0)

for i in range(100):
    if (N-3) in ng_list:
        if (N-2) in ng_list:
            if (N-1) in ng_list:
                break
            else:
                N -= 1
        else:
            N -= 2
    else:
        N -= 3

if N <= 0:
    print('YES')
else:
    print('NO')
