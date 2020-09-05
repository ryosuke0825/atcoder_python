A, B, T = map(int, input().split())

interval = B-A
year = B
while True:
    year += interval
    if year >= T:
        print(year)
        break
