N, K = map(int, input().split())
A = list(map(int, input().split()))

zumi_hash = {}
zumi = [-1]*(2*(10**5))
ima = 1
for i in range(K):
    # 行ったことある町を通る＝ループする
    if ima in zumi_hash:
        zumi[i] = ima
        break
    # 同じ町へテレポートしている
    if ima == A[ima-1]:
        print(ima)
        exit(0)
    zumi_hash[ima] = True
    zumi[i] = ima
    ima = A[ima-1]
else:
    print(ima)
    exit(0)

loop_e = zumi.index(-1)
loop_s = zumi.index(zumi[loop_e-1])
zan_loop = K-loop_s
loop = zumi[loop_s:loop_e-1]
amari = zan_loop % (len(loop))
print(loop[amari])
