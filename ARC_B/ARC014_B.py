N = int(input())
A = []
B = []

words = []
for _ in range(N):
    tmp = input()
    words.append(tmp)

for i in range(N):
    tmp = words[i]
    # 高橋くん（A)のターン
    if (i+1) % 2 != 0:
        if len(A) == 0:
            A.append(tmp)
        else:
            if B[-1][-1] == tmp[0]:
                if A.count(tmp) == 0 and B.count(tmp) == 0:
                    A.append(tmp)
                else:
                    print('LOSE')
                    break
            else:
                print('LOSE')
                break
    # 高橋クン（B)のターン
    else:
        if A[-1][-1] == tmp[0]:
            if A.count(tmp) == 0 and B.count(tmp) == 0:
                B.append(tmp)
            else:
                print('WIN')
                break
        else:
            print('WIN')
            break
else:
    print('DRAW')
