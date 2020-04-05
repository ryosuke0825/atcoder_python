from collections import deque

K = int(input())
dque = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

ans = 0
while True:
    v = dque.popleft()
    ans += 1
    if ans == K:
        print(v)
        exit(0)

    for i in range(-1, 2):
        # 10で割った余りを取得して、iを足す
        tmp = v % 10+i
        if not(0 <= tmp <= 9):
            continue
        dque.append(v*10+tmp)
