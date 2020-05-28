# N進数Nを10進数に変換する
def f(n):
    tmp = n
    ans = 0
    base = 1
    # 桁数だけループする
    while tmp:
        ans += tmp % 10*base
        base *= n
        tmp //= 10
    return ans


N = int(input())
for i in range(10, 10001):
    if f(i) == N:
        print(i)
        break
else:
    print(-1)
