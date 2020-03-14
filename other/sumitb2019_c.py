# 品物数を決めると合計金額は100*個数～105*個数の範囲となる
# xが範囲内にあれば買い方が存在する。なければしない。
x = int(input())

for i in range(1, 1000001):
    if 100*i <= x <= 105*i:
        print(1)
        break
else:
    print(0)
