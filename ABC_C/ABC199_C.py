N = int(input())
S = list(input())
Q = int(input())

# Q回のクエリを処理する
cnt = 0
for _ in range(Q):
    T, A, B = map(int, input().split())

    # クエリ1（入れ替え）
    if T == 1:
        # cntの偶数奇数
        if cnt % 2 == 0:
            # 偶数回前後入れ替えをしているのでそのまま
            a = S[A-1]
            b = S[B-1]
            S[A-1] = b
            S[B-1] = a
        else:
            # 奇数回前後入れ替えをしている
            if A <= N:
                A += N
            else:
                A -= N
            if B <= N:
                B += N
            else:
                B -= N
            a = S[A-1]
            b = S[B-1]
            S[A-1] = b
            S[B-1] = a

    else:
        # クエリ2（前後半入れ替え）
        # 最後にまとめてやる
        cnt += 1

ans = ''
if cnt % 2 == 0:
    ans = ''.join(S)
else:
    ans = ''.join(S[N:]) + ''.join(S[:N])
print(ans)
