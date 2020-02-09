h, w = map(int, input().split())
hw = []

first_end = ["#" for _ in range(w+2)]
hw.append(first_end)

for _ in range(h):
    one_line = list(input())
    one_line.insert(0, "#")
    one_line.append("#")
    hw.append(one_line)

hw.append(first_end)

for one_line in hw:
    print("".join(one_line))
