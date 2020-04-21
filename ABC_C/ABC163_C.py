import collections

# 入力
N = int(input())
A = list(map(int, input().split()))

# リストの中の各値が何個かあるかを連想配列化する
# ['a','b','d','b','e','a','c','d','b'] → {'a':2,'b':3,'c':1,'d':2,'e':1}
AC = collections.Counter(A)

# 1～Nまでの個数を出力する（rangeは第1引数から第2引数-1までの範囲）
# 例：range(1,5)→1,2,3,4
for i in range(1, N+1):
    # 連想配列にiと同じキーがあれば、その値を出力
    if i in AC:
        print(AC[i])

    # キーがない場合は0個ということなので、0を出力
    else:
        print(0)
