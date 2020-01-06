n = int(input())
A = []
X_Y = [[] for _ in range(n)]

for i in range(n):
    a = int(input())
    A.append(a)
    for j in range(a):
        x, y = map(int, input().split())
        # インデックスに合わせるためにx-1している
        tap = (x-1, y)
        X_Y[i].append(tap)

ans = 0

# bitの列挙、一つずつ探索する
for bit in range(1 << n):

    # 2進数にした時に1が何個あるかカウントする
    check = str(bin(bit)).count('1')

    for i in range(n):
        # 各bitが1の場合は正直者とする、0の場合は不親切な人なので確認は不要
        if (bit >> i) & 1 == 1:
            # X_Y[i]の中身が正直者には1, 不明者には0が向いているかを確認
            count = 0
            for obj in X_Y[i]:
                # 対象が嘘つきの場合
                if (obj[1] == 0) and (bit >> obj[0] & 1 == 0):
                    count += 1
                # 対象が正直者の場合
                elif (obj[1] == 1) and (bit >> obj[0] & 1 == 1):
                    count += 1
                else:
                    pass

            # 正直者の発言が正しい場合
            if count == A[i]:
                check -= 1

    # 全員の成否を確かめた後に、正直者の発言がすべて正しいか判定
    if check == 0:
        can = str(bin(bit)).count('1')
        # 正直者の発言が正しい場合はansを比較
        if ans <= can:
            ans = can
print(ans)
