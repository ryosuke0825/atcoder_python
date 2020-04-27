A, B, K, L = map(int, input().split())

# 個別で買うほうが安い場合
if A*L <= B:
    print(A*K)
    exit(0)

ans = 0
amari = 0

# セットの購入数を求める
ans = (K//L)*B
amari = K % L

# セットで揃わなかった分を個別で買うか、セットで買うか
if amari != 0:
    if A*amari <= B:
        ans += A*amari
    else:
        ans += B
print(ans)
