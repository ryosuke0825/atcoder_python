from collections import defaultdict

N = int(input())

dic = defaultdict(lambda: False)
ans = 'satisfiable'

for _ in range(N):
    T = input()

    # フラグを立たせる
    if not(dic[T]):
        dic[T] = True

    # 逆の文字を作る、!が付与されていない文字も取得する
    # aaa -> !aaa
    # !aaa -> aaa
    tt = ''
    koho = ''
    if T[0] == '!':
        tt = T[1:]
        koho = tt
    else:
        tt = '!'+T
        koho = T

    # 両方存在するか
    if dic[T] and dic[tt]:
        ans = koho

print(ans)
