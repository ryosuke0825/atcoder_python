n, a, b = map(int, input().split())
east_sum = 0
west_sum = 0

for _ in range(n):
    s, d = input().split()
    int_d = int(d)
    if int_d < a:
        int_d = a
    elif int_d > b:
        int_d = b

    if s == "East":
        east_sum += int_d
    else:
        west_sum += int_d

ans = ""
if east_sum == west_sum:
    print(0)
elif east_sum > west_sum:
    print("East", abs(east_sum-west_sum))
else:
    print("West", abs(east_sum-west_sum))
