N = int(input())

after_A = int(input())
a = 0
for _ in range(N-1):
    a = int(input())

    if a == after_A:
        print('stay')
    elif a < after_A:
        print('down', after_A-a)
    elif a > after_A:
        print('up', a-after_A)
    after_A = a
