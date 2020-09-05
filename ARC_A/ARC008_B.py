import collections
import math

N, M = map(int, input().split())
name = input()
kit = input()

# カウンターで各文字の個数を調べる
name_c = collections.Counter(name)
kit_c = collections.Counter(kit)

# kitからnameを作成できるか調べる
# nameに使われる全ての文字が1文字以上kitにあるか
for key in name_c.keys():
    if key in kit:
        pass
    else:
        print(-1)
        exit(0)

# 必要な個数を求める
# 各文字でnameに必要な文字数/kitに含まれる文字数を求める。切り上げた最大値が必要なkit数
ans = 1
for key in name_c.keys():
    ans = max(ans, math.ceil(name_c[key]/kit_c[key]))
print(ans)
