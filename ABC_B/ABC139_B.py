a, b = map(int, input().split())


if b == 1:
    print(0)
    exit(0)

ans = 1
tap = a
while tap < b:
    tap = tap + a - 1
    ans += 1

print(ans)
